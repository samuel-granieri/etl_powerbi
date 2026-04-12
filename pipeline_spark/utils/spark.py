from pyspark.sql import SparkSession

def create_spark_session(app_name: str) -> SparkSession:
    return (
        SparkSession.builder
        .appName(app_name)

        # delta
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

        # parquet compatibilidade
        .config("spark.sql.parquet.int96RebaseModeInWrite", "LEGACY")
        .config("spark.sql.parquet.datetimeRebaseModeInWrite", "LEGACY")

        # performance
        .config("spark.sql.shuffle.partitions", 8)
        .config("spark.sql.adaptive.enabled", "true")
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true")

        # delta otimização
        .config("spark.databricks.delta.schema.autoMerge.enabled", "true")
        .config("spark.databricks.delta.optimizeWrite.enabled", "true")
        .config("spark.databricks.delta.autoCompact.enabled", "true")

        # arquivos
        .config("spark.sql.files.maxPartitionBytes", "134217728")

        # arrow
        .config("spark.sql.execution.arrow.pyspark.enabled", "true")

        # debug
        .config("spark.sql.debug.maxToStringFields", 2000)

        # temp
        .config("spark.local.dir", "/tmp")

        .getOrCreate()
    )