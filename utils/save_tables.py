from delta.tables import DeltaTable
from pyspark.sql.functions import max as spark_max

def save_table(df, table_config, config, spark, layer):

    tabela_nome = table_config["name"]

    layer_path = config["storage"][layer]["path"]
    layer_format = config["storage"][layer]["format"]

    table_path = f"{layer_path}/{tabela_nome}"

    load_type = table_config.get("load_type", "full")
    strategy = table_config.get("incremental_strategy")
    merge_keys = table_config.get("merge_keys", [])
    incremental_column = table_config.get("incremental_column")

    print(f"\nProcessando tabela: {tabela_nome}")
    print(f"path: {table_path}")

    # --------------------
    # FULL LOAD
    # --------------------

    if load_type == "full":

        print("modo: FULL OVERWRITE")

        df.write \
            .format(layer_format) \
            .mode("overwrite") \
            .option("overwriteSchema", "true") \
            .save(table_path)

        return

    # --------------------
    # INCREMENTAL
    # --------------------

    if not DeltaTable.isDeltaTable(spark, table_path):

        print("primeira carga -> criando tabela delta")

        df.write \
            .format(layer_format) \
            .mode("overwrite") \
            .save(table_path)

        return

    # tabela já existe
    delta_table = DeltaTable.forPath(spark, table_path)

    # --------------------
    # APPEND
    # --------------------

    if strategy == "append":

        print("modo incremental: APPEND")

        df.write \
            .format(layer_format) \
            .mode("append") \
            .save(table_path)

        return

    # --------------------
    # MERGE
    # --------------------

    if strategy == "merge":

        print("modo incremental: MERGE")

        df_incremental = df

        # watermark
        if table_config.get("watermark"):

            print("usando watermark")

            max_watermark = (
                delta_table.toDF()
                .select(spark_max(incremental_column))
                .collect()[0][0]
            )

            print(f"ultimo valor de {incremental_column}: {max_watermark}")

            if max_watermark:

                df_incremental = df.filter(
                    df[incremental_column] > max_watermark
                )

        if df_incremental.count() == 0:

            print("sem novos dados")
            return

        merge_condition = " AND ".join(
            [f"target.{k} = source.{k}" for k in merge_keys]
        )

        (
            delta_table.alias("target")
            .merge(
                df_incremental.alias("source"),
                merge_condition
            )
            .whenMatchedUpdateAll()
            .whenNotMatchedInsertAll()
            .execute()
        )

        print("merge executado")

        return

    raise Exception(f"estratégia não suportada: {strategy}")