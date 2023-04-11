import clsprop


class Simple:
    @clsprop
    def name(cls):
        return cls.__name__


def test_simple():
    assert Simple.name == 'Simple'
