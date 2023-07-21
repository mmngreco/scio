# Docstrings

References:
- https://bwanamarko.alwaysdata.net/napoleon/format_exception.html
- https://www.datacamp.com/tutorial/docstrings-python
- https://stackoverflow.com/a/24385103
- https://sphinxcontrib-napoleon.readthedocs.io/en/latest/#google-vs-numpy
- https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy
- https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html


## Sphinx

```
def format_exception_Sphinx(etype, value, tb, limit=None):
    """
    Format the exception with a traceback.

    :arg etype:  exception type
    :type etype: str
    :arg value: exception value
    :type value: int
    :arg tb: traceback object
    :type tb: traceback
    :keyword limit: maximum number of stack frames to show [optional]
    :type limit: int or None
    :returns: out
    :rtype: list of strings
    :raises: AttributeError, KeyError

    A really great idea.  A way you might use me is

    >>> data = format_exception_Sphinx('stoopid', 1, ValueError)
    """
    return etype, value, tb
```

## Google

```
def format_exception_google(etype, value, tb, limit=None):
    """
    Format the exception with a traceback.

    Args:
       etype (str):  exception type
       value (int):  exception value
       tb (traceback): traceback object

    Keyword Args:
       limit (int or None):  maximum number of stack frames to show [optional]

    Returns:
       out:  list of strings

    Raises:
       AttributeError, KeyError

    A really great idea.  A way you might use me is

    >>> data = format_exception_google('wow', 999, KeyError)
    """
    return etype, value, tb
```


## NumpyDoc

```
def format_exception_numpy(etype, value, tb, limit=None):
    """
    Format the exception with a traceback.

    Parameters
    ----------
    etype : str
        exception type
    value : int
        exception value
    tb : traceback
        traceback object
    limit : int or None
        maximum number of stack frames to show

    Returns
    -------
    out : list of strings
        list of strings

    Raises
    ------
    AttributeError, KeyError
        When value doesn't exists.


    See Also
    --------
    numpy : a numerical package

    Notes
    -----
    This is an example of autodoc using numpydoc, the Numpy documentation format
    with the numpydoc extension [1]_

    This explanation of the column headers is not complete, for an exhaustive
    specification see [2]_.

    References
    ----------
    .. [1] `numpydoc <https://github.com/numpy/numpy/tree/master/doc/sphinxext>`_, \
        Numpy Documentation.
    .. [2] `Sphinx <http://sphinx-doc.org/domains.html#domains>`_, Sphinx Domains \
        Documentation.

    Examples
    --------
    >>> data = format_exception_numpy('dumb', 0, IOError)
    """
    return etype, value, tb
```

# Summary

NumpyDoc:
- Complete (Raises, Notes, References, ...)
- Wide used (Scientific stack of Python)
- Maintained by numpy
- Human readable
- Sphinx compatible (using napoleon)
- rST markup

Google:
- Maintained by google
- Human readable
- Sphinx compatible (using napoleon)


Sphinx:
- Created by Sphinx

