"""Reusable utilities across the project"""
from typing import Any, Callable, TypeVar, cast

__author__ = 'Aaron Alphonso'
__email__ = 'alphonsoaaron1993@gmail.com'

import os
import json
from functools import wraps


def clear_screen() -> None:
    """Clears the console"""
    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


def strike_through(text: str) -> str:
    """Returns a strike-through version of the input text"""
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


def create_data_dir_if_not_exists() -> None:
    """Creates a data directory if it does not exist. The data directory holds all game relevant data files"""
    from housie.constants import DATA_DIR
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def save_json(data: Any, filename: str) -> None:
    """Saves the input data to a file"""
    create_data_dir_if_not_exists()
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_json(filename: str) -> Any:
    """Loads and returns the json data from a file as json. If the file is missing, returns None"""
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return None


F = TypeVar('F', bound=Callable[..., Any])


def dynamic_doc(func: F) -> F:
    """Decorator to insert the actual values of variables into the docstrings of certain methods.

    This is so that we can insert certain values from our constants into our docstrings to make them more accurate
    """

    @wraps(func)
    def wrapper(*args, **kwargs):  # type: ignore
        """No added behavior in the wrapper apart from the formatted docstring"""
        return func(*args, **kwargs)

    # Format the original docstring with the constant values
    from housie import constants
    wrapper.__doc__ = func.__doc__.format(**constants.__dict__)  # type: ignore
    return cast(F, wrapper)
