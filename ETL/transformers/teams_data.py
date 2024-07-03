from pyspark.sql.types import *

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    spark = kwargs['spark']
    df = data[1]

    needed_columns = ['code', 'id', 'name', 'short_name', 'strength',\
                    'strength_overall_away', 'strength_overall_home',\
                    'strength_attack_away', 'strength_attack_home',\
                    'strength_defence_away', 'strength_defence_home']
    df = df.loc[:, needed_columns]
    schema = StructType([
            StructField("code", StringType(), True),
            StructField("id", StringType(), True),
            StructField("name", StringType(), True),
            StructField("short_name", StringType(), True),
            StructField("strength", IntegerType(), True),
            StructField("strength_overall_away", IntegerType(), True),
            StructField("strength_overall_home", IntegerType(), True),
            StructField("strength_attack_away", IntegerType(), True),
            StructField("strength_attack_home", IntegerType(), True),
            StructField("strength_defence_away", IntegerType(), True),
            StructField("strength_defence_home", IntegerType(), True)
        ])

    df_spark = spark.createDataFrame(df, schema=schema)
    df_spark = df_spark.withColumnRenamed('name', 'team_name')

    return df_spark.toPandas()

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
