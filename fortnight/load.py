import pkg_resources
import pandas as pd


def load():

    # Load the data from the package
    data_path = pkg_resources.resource_filename('fortnight', 'datasets/weather.csv')

    # Return the data
    return pd.read_csv(data_path, header = 0)