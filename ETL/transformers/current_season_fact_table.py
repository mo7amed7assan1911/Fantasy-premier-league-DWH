from pyspark.sql import functions as F
from pyspark.sql.types import *


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    spark = kwargs['spark']
    df = data[0]
    schema = StructType([
            StructField("element", StringType(), False),
            StructField("fixture", StringType(), False),
            StructField("opponent_team", StringType(), False),
            StructField("total_points", IntegerType(), False),
            StructField("was_home", BooleanType(), False),
            StructField("kickoff_time", StringType(), False),
            StructField("team_h_score", IntegerType(), False),
            StructField("team_a_score", IntegerType(), False),
            StructField("round", StringType(), False),
            StructField("minutes", IntegerType(), False),
            StructField("goals_scored", IntegerType(), False),
            StructField("assists", IntegerType(), False),
            StructField("clean_sheets", IntegerType(), False),
            StructField("goals_conceded", IntegerType(), False),
            StructField("own_goals", IntegerType(), False),
            StructField("penalties_saved", IntegerType(), False),
            StructField("penalties_missed", IntegerType(), False),
            StructField("yellow_cards", IntegerType(), False),
            StructField("red_cards", IntegerType(), False),
            StructField("saves", IntegerType(), False),
            StructField("bonus", IntegerType(), False),
            StructField("bps", IntegerType(), False),
            StructField("influence", StringType(), False),
            StructField("creativity", StringType(), False),
            StructField("threat", StringType(), False),
            StructField("ict_index", StringType(), False),
            StructField("starts", IntegerType(), False),
            StructField("expected_goals", StringType(), False),
            StructField("expected_assists", StringType(), False),
            StructField("expected_goal_involvements", StringType(), False),
            StructField("expected_goals_conceded", StringType(), False),
            StructField("value", IntegerType(), False),
            StructField("transfers_balance", IntegerType(), False),
            StructField("selected", IntegerType(), False),
            StructField("transfers_in", IntegerType(), False),
            StructField("transfers_out", IntegerType(), False)
        ])

    spark_df = spark.createDataFrame(df, schema=schema)
    spark_df = spark_df.withColumn('kickoff_time', F.to_timestamp(spark_df.kickoff_time))

    float_columns = ['bps', 'influence', 'creativity', 'threat', 'ict_index']
    for col in float_columns:
        spark_df = spark_df.withColumn(col, spark_df[col].cast(FloatType()))

    spark_df = spark_df.withColumn('value', (spark_df.value / 10).cast(FloatType())).\
                withColumnRenamed('round', 'GW').\
                withColumnRenamed('value', 'price').\
                withColumnRenamed('minutes', 'minutes_played')

    return spark_df.toPandas()


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'