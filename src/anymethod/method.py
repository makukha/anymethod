class anymethod(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls=None):
        owner = obj if obj is not None else cls
        return self.func.__get__(owner, cls)

    @property
    def __isabstractmethod__(self):
        return getattr(self.func, '__isabstractmethod__', False)
