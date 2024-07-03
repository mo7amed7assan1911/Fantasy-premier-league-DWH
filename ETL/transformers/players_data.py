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
                    'web_name', 'element_type', 'team', 'team_code',\
                    'dreamteam_count', 'news',
                    ]
    
    df = df.loc[:, needed_columns]
    df['news'].replace('', 'No news', inplace=True)

    conversion_map = {
        "code": str,
        "id": str,
        "element_type": str,
        "team": str,
        "team_code": str,
    }
    df.insert(loc=2, column='full_name', value=df['first_name'] + " " + df['second_name'])
    df.drop(columns=['first_name', 'second_name'], inplace=True)
    df = df.astype(conversion_map)
    print(df.info())
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
