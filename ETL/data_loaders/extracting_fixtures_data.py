import io
import pandas as pd
import requests
import json

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://fantasy.premierleague.com/api/fixtures/'  # Correct URL for fixtures
    response = requests.get(url)
    data = json.loads(response.text)
    fixtures_df = pd.DataFrame(data)

    fixtures_df.drop(columns='stats', inplace=True)
    return fixtures_df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
