import io
import pandas as pd
import requests
import json
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    spark = SparkSession.builder.appName('FPL_ingestion').getOrCreate()
    kwargs['context']['spark'] = spark
    
    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    response = requests.get(url)

    # Convert JSON data to a python object
    data = json.loads(response.text)

    players_df = pd.DataFrame(data['elements'])
    teams_df = pd.DataFrame(data['teams'])
    positions_of_players_df = pd.DataFrame(data['element_types'])
    gameweeks_df = pd.DataFrame(data['events'])

    # all_data_dict = {
    #     'players': players_df,
    #     'teams': teams_df,
    #     'element_types': element_types_df,
    #     'events': events_df
    # }
    return players_df, teams_df, positions_of_players_df, gameweeks_df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
