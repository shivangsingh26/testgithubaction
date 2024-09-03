from src.math_operations import add, sub, mul

def test_add():
    assert add(4,5)==9
    assert add(-1,1)==0

def test_sub():
    assert sub(4,5)==-1
    assert sub(-1,1)==-2

def test_mul():
    assert mul(4,5)==20
    assert mul(-1,1)==-1


