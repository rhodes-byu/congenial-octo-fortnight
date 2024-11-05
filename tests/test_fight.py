from fortnight import sum_count
import numpy as np

def test_sum_count_list():
    assert sum_count([1, 2, 3, 4, 5]) == (15, 5)
    assert sum_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (55, 10)


def test_sum_count_np_array():
    assert sum_count(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) == (66, 'large list')
    assert sum_count(np.array([1, 2, 3, 4, 5])) == (15, 5)