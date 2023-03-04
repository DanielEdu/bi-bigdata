from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master('local[*]')
    .appName('my_spark_app_v1')
).getOrCreate()

spark.sparkContext.setLogLevel('WARN')

# Leemos el archivo de datos en una variable
df_pokemon = (
    spark.read.format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("/Users/Shared/data/pokemon.csv")
    )

df_pokemon.show(5,False)

# DF Movies
df_movie = (
    spark.read.format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("/Users/Shared/data/movie.csv")
    )

df_movie.show(5,False)


df_pokemon_legendary = df_pokemon.filter(df_pokemon["Legendary"] == True)


df_pokemon_legendary.write.format("csv") \
    .mode("overwrite") \
    .option("header", "true") \
    .save("/Users/Shared/data/out/pokemon_legendary")


df_movie.write.format("csv") \
    .mode("overwrite") \
    .option("header", "true") \
    .save("/Users/Shared/data/out/df_movie")


spark.stop()
exit()