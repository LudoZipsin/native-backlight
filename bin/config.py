"""This module contain all the config utilies and should be used as a
config reader module to get the inner tweak of the application
"""

import configparser


# config
_CONFIG_FILE = "/opt/native-backlight/config"
#  _CONFIG_FILE = "config"

# config - Network
_CFG_NETWORK_SEC = "NETWORK"
_CFG_PORT = "port"

# config - Other
_CFG_OTHER_SEC = "OTHER"
_CFG_MAX = "max"
_CFG_DEFAULT = "default"
_CFG_THRESHOLD = "threshold"
_CFG_STEP = "step"
_CFG_BRIGHTNESS_FILE = "brightness_file"


_CONFIG = configparser.ConfigParser()
_CONFIG.read(_CONFIG_FILE)


def communication_port() -> int:
    """Return the port used to communicate over zerorpc
    """
    return _CONFIG[_CFG_NETWORK_SEC].getint(_CFG_PORT)


def max_brightness() -> int:
    """Return the max value allowed for the brightness
    """
    return _CONFIG[_CFG_OTHER_SEC].getint(_CFG_MAX)


def default_brightness() -> int:
    """Return the default value for the brightness
    """
    return _CONFIG[_CFG_OTHER_SEC].getint(_CFG_DEFAULT)


def time_threshold() -> int:
    """Return the threshold time. This time is used
    to prevent to fast bightness change
    """
    return _CONFIG[_CFG_OTHER_SEC].getint(_CFG_THRESHOLD)


def brightness_step() -> int:
    """Return the increment and decrement value used to
    increase or decrease the brightness
    """
    return _CONFIG[_CFG_OTHER_SEC].getint(_CFG_STEP)


def brightness_file_name() -> str:
    """Return the name of the brightness control file which is
    used by linux system to manage brightness at low level
    """
    return _CONFIG[_CFG_OTHER_SEC][_CFG_BRIGHTNESS_FILE]
