from pyspark.sql import SparkSession

# Criar uma SparkSession
spark = SparkSession.builder \
    .appName("MeuAplicativoPySpark") \
    .getOrCreate()

# Criar um DataFrame
data = [("João", 25), ("Alice", 30), ("Bob", 35)]
df = spark.createDataFrame(data, ["Nome", "Idade"])

# Mostrar o DataFrame
df.show()

# Parar a SparkSession
spark.stop()
