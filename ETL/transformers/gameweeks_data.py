from pyspark.sql import functions as F
from pyspark.sql.types import *

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    spark = kwargs['spark']
    df = data[3]

    needed_columns = ['id', 'name', 'deadline_time', 'highest_score',\
    'average_entry_score','most_selected', 'most_transferred_in',\
    'top_element', 'most_captained', 'most_vice_captained']

    df = df.loc[:, needed_columns]
    schema = StructType([
                StructField('id', StringType(), True),\
                StructField('name', StringType(), True),\
                StructField('deadline_time', StringType(), True),\
                StructField('highest_score', IntegerType(), True),\
                StructField('average_entry_score', IntegerType(), True),\
                StructField('most_selected', StringType(), True),\
                StructField('most_transferred_in', StringType(), True),\
                StructField('top_element', StringType(), True),\
                StructField('most_captained', StringType(), True),\
                StructField('most_vice_captained', StringType(), True)])

    df_spark = spark.createDataFrame(df, schema=schema)
    df_spark = df_spark.withColumn('deadline_time', F.to_timestamp(df_spark.deadline_time)).\
                withColumnRenamed('name', 'gw_name')

    return df_spark.toPandas()

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
