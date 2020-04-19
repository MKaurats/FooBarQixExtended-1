from FooBarQixExtendedCode import FooBar

def FooBarCheck(X, ReturnedXVal):
    ReturnXVal = FooBar(X)
    assert ReturnXVal == ReturnedXVal

def test_X0():
    FooBarCheck(0, "Foo Bar")

def test_X1():
    FooBarCheck(1, "1")

def test_X3():
    FooBarCheck(3, "Foo")

def test_X5():
    FooBarCheck(5, "Bar")

def test_X98():
    FooBarCheck(98, "98")

def test_X99():
    FooBarCheck(99, "Foo")

def test_X100():
    FooBarCheck(100, "Bar")
 
