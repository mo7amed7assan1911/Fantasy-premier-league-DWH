if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    spark = kwargs['spark']
    df = spark.createDataFrame(data)
    print(df.printSchema())
    return data

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
    assert output.isna().sum().sum() == 0, 'There are null values'
    assert output.duplicated().sum() == 0,  'There are duplicates'