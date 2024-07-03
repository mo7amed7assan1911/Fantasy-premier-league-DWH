
import io
import pandas as pd
import requests
import json
import os
import kwargs
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.master(os.getenv('SPARK_MASTER_HOST', 'local')).getOrCreate()
spark = kwargs.get('spark')


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    rdd = spark.sparkContext.parallelize([1, 2, 3])
    # Make a request to GET the data from the FPL API
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    response = requests.get(url)

    # Convert JSON data to a python object
    data = json.loads(response.text)

    # Create pandas DataFrame from JSON player data
    players_df = pd.DataFrame.from_dict(data['elements'])
    teams_df = pd.DataFrame.from_dict(data['teams'])
    element_types_df = pd.DataFrame.from_dict(data['element_types'])
    events_df = pd.DataFrame.from_dict(data['events'])

    return players_df, teams_df, element_types_df, events_df, rdd
        

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
