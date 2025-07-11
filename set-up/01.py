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
