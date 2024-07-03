from pyspark.sql.types import *

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    spark = kwargs['spark']
    df = data[0]
    needed_columns = ['code', 'id', 'first_name', 'second_name',\
                    'web_name', 'element_type', 'team', 'team_code', 'total_points',\
                    'selected_by_percent', 'transfers_in', 'transfers_out', 'minutes',\
                    'goals_scored', 'assists', 'clean_sheets',\
                    'own_goals', 'penalties_saved', 'penalties_missed',
                    'yellow_cards', 'red_cards', 'bonus', 'ict_index',
                    'goals_conceded_per_90', 'form_rank', 'points_per_game_rank',\
                    'selected_rank', 'dreamteam_count', 'news', 'points_per_game',
                    ]
    
    df = df.loc[:, needed_columns]
    df['news'].replace('', 'No news', inplace=True)

    conversion_map = {
        "code": str,
        "id": str,
        "element_type": str,
        "team": str,
        "team_code": str,
        "selected_by_percent": float,
        "ict_index": float,
        "points_per_game": float
    }

    df = df.astype(conversion_map)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
