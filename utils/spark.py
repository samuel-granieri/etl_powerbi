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

        # debug
        .config("spark.sql.debug.maxToStringFields", 2000)

        # temp dir
        .config("spark.local.dir", "/tmp/spark-temp")

        # reduzir arquivos temporários
        .config("spark.sql.shuffle.partitions", 8)
        .config("spark.default.parallelism", 8)

        # evita alguns locks
        .config("spark.cleaner.referenceTracking.cleanCheckpoints", "true")

        .getOrCreate()
    )