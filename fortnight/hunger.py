def hungry(is_hungry=True):
    """
    Prints and returns a message based on the hunger status.

    Parameters
    ----------
    is_hungry : bool, optional
        A boolean indicating if the user is hungry (default is True).

    Returns
    -------
    str
        The message "I am hungry" if `is_hungry` is True.

    Raises
    ------
    Exception
        If `is_hungry` is False, raises an Exception with the message "I am not hungry".

    Examples
    --------
    >>> hungry()
    I am hungry
    'I am hungry'

    >>> hungry(is_hungry=False)
    Traceback (most recent call last):
        ...
    Exception: I am not hungry
    """
    
    if is_hungry:
        print("I am hungry")
        return "I am hungry"
    else:
        raise Exception("I am not hungry")
