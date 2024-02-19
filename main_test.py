from main import add,sub,mul,div


def test_add():
    assert add(1,2) == 3
    assert add(5,10) == 15
    assert add(60,10) == 70


def test_sub():
    assert sub(2,3) == -1
    assert sub(4,2) == 2

def test_mul():
    assert mul(1,10) == 10



def test_div():
    assert div(10,2) == 5
    assert div(100,10) == 10
