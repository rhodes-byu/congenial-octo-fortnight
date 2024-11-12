import pkg_resources
import pandas as pd


def load():
    """
    Loads weather data from the package's dataset directory.

    This function retrieves the `weather.csv` file located in the `datasets` folder within the 
    `fortnight` package and returns it as a pandas DataFrame.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the weather data, with headers taken from the first row of the CSV file.

    Examples
    --------
    >>> df = load()
    >>> df.head()
       # Displays the first few rows of the weather data
    """
    
    # Load the data from the package
    data_path = pkg_resources.resource_filename('fortnight', 'datasets/weather.csv')

    # Return the data
    return pd.read_csv(data_path, header=0)