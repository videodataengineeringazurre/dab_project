import os
import sys
import pytest

sys.path.append(os.getcwd()) 

@pytest.fixture()
def spark():
    try:
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.remote(cluster_id="1208-064343-26hl3na3").getOrCreate()
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark=SparkSession.builder.getOrCreate() 
    
        except ImportError:  
            raise ImportError("Could not import SparkSession from either databricks.connect or pyspark.sql. Please ensure that PySpark or Databricks Connect is installed.")         
        return spark