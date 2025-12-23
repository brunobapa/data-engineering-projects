from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

def main():
    spark = SparkSession.builder \
        .appName("Spark Big Data Example") \
        .getOrCreate()

    df = spark.read.csv(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv",
        header=True,
        inferSchema=True
    )

    df_clean = df.dropna()

    result = (
        df_clean
        .groupBy("day")
        .agg(count("*").alias("total_registros"))
        .orderBy(col("total_registros").desc())
    )

    result.show()

    spark.stop()

if __name__ == "__main__":
    main()
