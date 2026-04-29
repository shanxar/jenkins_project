import pytest 
from calc import Calc 

@pytest.fixture(scope="module")
def setup():
    print("In Setup")
    return Calc()

def test_add(setup):
    assert setup.add(2,1)==3

def test_sub(setup):
    assert setup.sub(2,1) == 1