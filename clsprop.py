import sys


class clsprop(property):
    """
    Just like property but for class objects.

    From https://stackoverflow.com/a/39542816/43839
    """
    def __get__(self, obj, objtype=None):
        return super(clsprop, self).__get__(objtype)

    def __set__(self, obj, value):
        super(clsprop, self).__set__(type(obj), value)

    def __delete__(self, obj):
        # This is never called; there seems to be no way to make
        # this work.
        super(clsprop, self).__delete__(type(obj))


sys.modules[__name__] = clsprop
