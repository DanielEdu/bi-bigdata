package demo.spark

import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.log4j.{Level, Logger}

object SparkDemo {

  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder
      .master("local[*]")
      .appName("SparkScalaDemo")
      .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")


    println("Hello, Spark")

    val sparkVersion = spark.version
    val scalaVersion = util.Properties.versionNumberString
    val javaVersion = System.getProperty("java.version")

    println("SPARK VERSION = " + sparkVersion)
    println("SCALA VERSION = " + scalaVersion)
    println("JAVA  VERSION = " + javaVersion)

    val df_pokemon = read_data(spark, "/Users/Shared/data/pokemon.csv")
    val df_movie = read_data(spark, "/Users/Shared/data/movie.csv")
    df_pokemon.show(5, truncate = false)
    df_movie.show(5, truncate = false)

  }

  def read_data(spark: SparkSession, path: String): DataFrame = {
    val df = (
      spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(path)
      )
    df
  }

}
