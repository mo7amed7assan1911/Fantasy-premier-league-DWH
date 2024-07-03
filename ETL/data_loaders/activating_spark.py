import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    spark = kwargs.get('spark')

    data = [("Alice", 28), ("Bob", 22), ("Catherine", 33)]
    columns = ["Name", "Age"]
    # Create a DataFrame
    df = spark.createDataFrame(data, columns)
    df2 = df.toPandas()
    print(df.show())
    return df2

# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
