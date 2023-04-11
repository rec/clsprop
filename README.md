Works just like @property for classes, except deleters don't work (and are
perhaps impossible).

Inspired by https://stackoverflow.com/a/39542816/43839

## Example

    import clsprop

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


### [API Documentation](https://rec.github.io/clsprop#clsprop--api-documentation)
