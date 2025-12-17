from databricks.connect import DatabricksSession

spark=DatabricksSession.builder.remote(cluster_id="1208-064343-26hl3na3").getOrCreate()
spark.sql("select 1").show()