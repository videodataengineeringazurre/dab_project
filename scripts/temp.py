from databricks.connect import DatabricksSession

spark=DatabricksSession.builder.remote().getOrCreate()
spark.sql("select 1").show()