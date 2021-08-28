
def get_k_v(d):
    return d.items()[0] if d.items() else (None, None)


def deprecated(msg=None):
    def wrapped(func):
        def inner(*args, **kwargs):
            import warnings;
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn(
                msg or '%s() is deprecated' % func.__name__,
                category=DeprecationWarning
            )
            warnings.simplefilter('default', DeprecationWarning)
            return func(*args, **kwargs)
        return inner
    return wrapped
