"""Task 3"""


class Observable:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__,
                           (', '.join('%s=%s' % (key, val) for (key, val)
                                      in self.__dict__.items()
                                      if not key.startswith('_'))))


class X(Observable):
    pass


x = X(foo=1, bar=5, _baz=12, name='Amok', props=('One', 'two'))
print(x.name)
print(x)
