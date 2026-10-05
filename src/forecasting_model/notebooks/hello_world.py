# Databricks notebook source

print("Hello from my Databricks bundle!")

# COMMAND ----------

df = spark.range(10)
display(df)