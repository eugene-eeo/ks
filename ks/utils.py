"""
    ks.utils
    ~~~~~~~~
    Implements some helper methods that are commonly
    used throughout the ks library.
"""


def pipe(functions, data):
    """
    Pipe functions onto data, returning a value that
    is obtained by calling the consecutive functions
    with the return value of the previous function.

    :param functions: Iterable of functions.
    :param data: An object to pipe.
    """
    for func in functions:
        data = func(data)
    return data
