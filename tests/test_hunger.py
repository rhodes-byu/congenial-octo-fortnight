from fortnight import hungry
import pytest

def test_hungry():
    assert hungry() == "I am hungry"

def test_hungry_not():
    with pytest.raises(Exception) as e:
        hungry(False)
    assert str(e.value) == "I am not hungry"


# def test_hungry_will_fail():
#     assert hungry(True) == "I am not hungry"
    

