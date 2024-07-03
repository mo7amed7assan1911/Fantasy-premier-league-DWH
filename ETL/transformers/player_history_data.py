from pyspark.sql.types import *

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(data)
    df = data[1]
    df = df.loc[:, :'bonus']
    df['element_code'] = df['element_code'].astype(str)
    
    # converting costs such as => 55 to 5.5
    df[['start_cost', 'end_cost']] = df[['start_cost', 'end_cost']].apply(lambda x: x / 10)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
