import numpy as np
import pandas as pd


def sum_count(some_list):

    """
    sum_count accepts a list or np.array and returns the sum and length of the array.

    Parameters:
    -----------

    some_list: list or np.array
        A list of numbers or an array of numbers.

    Returns:
    --------

    tuple
        The first entry is the sum, the second the length.

    Examples
    --------
    >>> import numpy as np
    >>> # Small list example
    >>> small_list = [1, 2, 3, 4, 5]
    >>> sum_count(small_list)
    (15, 5)
    
    >>> # Large list example
    >>> large_list = np.arange(15)
    >>> sum_count(large_list)
    (105, 'large list')
    """
    
    sum_ = np.sum(some_list)
    count_ = len(some_list)

    if count_ > 10:
        return sum_, 'large list'

    return sum_, count_