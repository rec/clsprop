"""
🏫 `clsprop`: A decorator for class properties 🏫

Works just like @property for classes, except deletions don't work.

## Example

    class Full:
        _name = 'fool'

        @clsprop
        def name(cls):
            return cls._name

        @name.setter
        def name(cls, name):
            cls._name = name

        # Unfortunately, the deleter never gets called
        @name.deleter
        def name(cls, name):
            raise ValueError('Cannot delete name')

    assert Full.name == 'fool'

    Full.name = 'foll'
    assert Full.name == 'foll'

    del Full.name  # oh, well
"""

import sys


class clsprop(property):
    """
    Just like property but for class objects.

    From https://stackoverflow.com/a/39542816/43839
    """
    def __get__(self, obj, objtype=None):
        return super().__get__(objtype)

    def __set__(self, obj, value):
        super().__set__(type(obj), value)

    def __delete__(self, obj):
        # This is never called; there seems to be no way to make
        # this work.
        super().__delete__(type(obj))


sys.modules[__name__] = clsprop
