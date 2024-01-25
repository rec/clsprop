import pytest

import clsprop

BUG_FIXED = False


class Simple:
    @clsprop
    def name(cls):
        return cls.__name__


def test_simple():
    assert Simple.name == 'Simple'


class Full:
    _name = 'fool'

    @clsprop
    def name(cls):
        return cls._name

    @name.setter
    def name(cls, name):
        cls._name = name

    @name.deleter
    def name(cls, name):
        raise ValueError('Cannot delete name')


def test_full():
    assert Full.name == 'fool'

    Full.name = 'foll'
    assert Full.name == 'foll'

    if BUG_FIXED:
        with pytest.raises(ValueError) as e:
            del Full.name
        assert e.value.args == ('Cannot delete name',)
    else:
        del Full.name
        with pytest.raises(AttributeError) as e:
            Full.name
        assert e.value.args == ("type object 'Full' has no attribute 'name'",)
