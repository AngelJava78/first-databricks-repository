# Databricks notebook source
print("Hello world")

# COMMAND ----------

# MAGIC %sh
# MAGIC echo "Hola Angel"

# COMMAND ----------

display(dbutils.fs.ls("/"))

# COMMAND ----------

accessKey=dbutils.secrets.get(scope="kvs-accessKey-dbx-dev-eastus", key="kvs-accessKey-dbx-dev-eastus")
print(accessKey)

# COMMAND ----------

spark.conf.set("fs.azure.account.key.stdbxdeveastus01.dfs.core.windows.net", accessKey)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@stdbxdeveastus01.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@stdbxdeveastus01.dfs.core.windows.net/movie.csv"))
