
def FooBar( X ):
    if (X % 3) == 0 and (X % 5) == 0:
        return "Foo Bar"
    if (X % 3) == 0:
        return "Foo"
    if (X % 5) == 0:
        return "Bar"
    else:
        return str(X)
