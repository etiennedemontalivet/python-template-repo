"""Some cool functions to show nothing but a test"""


def my_sum(a: float, b: float) -> float:
    """Sum of two floats

    Parameters
    ----------
    a : float
        First value to sum
    b : float
        Second value to sum

    Returns
    -------
    float
        The sum of ``a`` and ``b``

    See also
    --------
    MyClass

    Example
    -------
    >>> from py_template_poetry.module_2 import my_sum
    >>> a = 5
    >>> c = 6
    >>> my_sum(a,c)
    """
    return a + b


# pylint: disable=anomalous-backslash-in-string
class MyClass:
    """Fake class that performs basic operations

    You can add details here or a unicorn from `here <https://www.asciiart.eu/mythology/unicorns>`_

    .. code-block::

                            |))    |))
        .             |  )) /   ))
        \\   ^ ^      |    /      ))
        \\(((  )))   |   /        ))
        / G    )))  |  /        ))
        |o  _)   ))) | /       )))
        --' |     ))`/      )))
            ___|              )))
        / __\             ))))`()))
        /\@   /             `(())))
        \/   /  /`_______/\   \  ))))
            | |          \ \  |  )))
            | |           | | |   )))
            |_@           |_|_@    ))
            /_/           /_/_/




    Parameters
    ----------
    a : float
        A first value

    b : float
        A second value


    Attributes
    ----------
    a : float
        The first value

    b : float
        The second value

    prod : float
        The product ``a*b``


    See also
    --------
    my_sum


    Notes
    -----
    Important note can be added here !


    References
    ----------
    Or a nice reference to an article or whatever


    Examples
    --------
    >>> from py_template_poetry.module_2 import MyClass, my_sum
    >>> a = 3
    >>> b = 6
    >>> my_class = MyClass(a, b)
    >>> my_sum(a, b) == my_class.my_inside_sum()
    """

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def my_inside_sum(self) -> float:
        """Sum ``a`` and ``b``

        Returns
        -------
        float
            Sum of ``a`` and ``b``
        """
        return self.a + self.b

    def k_sum(self, k: float) -> float:
        """``k`` times the sum

        Parameters
        ----------
        k : float
            Gain to multiply the sum

        Returns
        -------
        float
            ``k`` times the sum
        """
        return k * self.my_inside_sum()
