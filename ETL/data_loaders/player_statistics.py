import io
import pandas as pd
import requests
import json

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

base_url = "https://fantasy.premierleague.com/api/element-summary/{player_id}"
def feach_summary(player_id):
    """
        function that takes player id and returns his history data.
    """
    response = requests.get(base_url.format(player_id=player_id))
    return response.json()

all_players_current = []
all_players_previous = []


@data_loader
def load_data_from_api(df, *args, **kwargs):
    players_ids = df.id
    extracted_players = 0
    number_of_all_players = len(df.id)

    for id in players_ids:
        data = feach_summary(id)
        current_season = data['history']
        previous_seasons = data['history_past']

        all_players_current.extend(current_season)
        all_players_previous.extend(previous_seasons)

        if extracted_players % 50 == 0:
            print(f'Extracted {extracted_players}/{number_of_all_players}')
        
        extracted_players += 1

    current_season_df = pd.DataFrame(all_players_current)
    previous_seasons_df = pd.DataFrame(all_players_previous)
    return current_season_df, previous_seasons_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
