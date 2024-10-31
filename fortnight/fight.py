import numpy as np
import pandas as pd


def sum_count(some_list):

    """
    sum_count accepts a list or np.array and returns the sum and length of the array.

    Parameters:
    ----------

    some_list: list or np.array
        A list of numbers or an array of numbers.

    Returns:
    -------

    tuple
        The first entry is the sum, the second the length.
    """
    
    sum_ = np.sum(np.asarray(some_list))
    count_ = len(some_list)

    return sum_, count_