"""This module provide some utils functions to help declutered the
main server file.
"""

import time

import config


def timestamp() -> int:
    """Return the current timestamp in millisecond
    """
    return int(round(time.time() * 1000))


def brightness_writer(value: int) -> None:
    """Used to write the brightness value inside the appropriate file
    """
    # TODO function body
    pass


def brightness_increment(incr: int) -> int:
    """Increment the current brightness by 'incr'
    and return the new brightness value
    """
    # TODO function body
    pass


def brightness_drecrement(decr: int) -> int:
    """Decrement the current brightness by 'decr'
    and return the new brightness value
    """
    # TODO function body
    pass
