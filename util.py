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
    if not value:
        raise Exception("The content of 'value' can't be null")
    elif not isinstance(value, int):
        raise Exception("The value must be integer")
    else:
        with open(config.brightness_file_name(), 'r+') as sys_file:
            sys_file.seek(0)
            sys_file.write(str(value))
            sys_file.truncate()
            sys_file.close()


def brightness_increment(incr: int) -> int:
    """Increment the current brightness by 'incr'
    and return the new brightness value
    """
    if not incr:
        raise Exception("The content of 'incr' can't be null")
    elif not isinstance(incr, int):
        raise Exception("The increment must be integer")
    else:
        with open(config.brightness_file_name(), 'r+') as sys_file:
            brightness = int(sys_file.read())
            brightness += incr
            if brightness > config.max_brightness():
                brightness = config.max_brightness()
            sys_file.seek(0)
            sys_file.write(str(brightness))
            sys_file.truncate()
            sys_file.close()
            return brightness


def brightness_decrement(decr: int) -> int:
    """Decrement the current brightness by 'decr'
    and return the new brightness value
    """
    if not decr:
        raise Exception("The content of 'decr' can't be null")
    elif not isinstance(decr, int):
        raise Exception("The decrement must be integer")
    else:
        with open(config.brightness_file_name(), 'r+') as sys_file:
            brightness = int(sys_file.read())
            brightness -= decr
            if brightness < 0:
                brightness = 0
            sys_file.seek(0)
            sys_file.write(str(brightness))
            sys_file.truncate()
            sys_file.close()
            return brightness
