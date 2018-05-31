#! /usr/bin/env python3

"""This is the main file for the server part of the native brightness
controller. It aims to provide a communication interface suitable to
let client control the brightness without tempering with file permission
on the brightness system file.

This file should be run as root if you want it to work properly.
"""


import zerorpc

from tendo import singleton

import config
import util


class MessageHandler(object):
    """This is the mane message handler to handle message
    received by clients
    """

    def __init__(self):
        self.last_change = util.timestamp()

    def _validate_time(self) -> bool:
        """Check wether we can updatime the brightness acording to the last
        time it was changed
        """
        return (util.timestamp() - self.last_change) > config.time_threshold()

    def _apply(self, func, *arg) -> int:
        """apply the given function with the given args
        functioon expected:
            * brightness_writer
            * brightness_increment
            * brightness_drecrement
        """
        result = -1
        if self._validate_time():
            self.last_change = util.timestamp()
            result = func(*arg)
        return result

    def reset(self):
        """Reset to default value the brightness of the monitor
        """
        try:
            self._apply(util.brightness_writer, config.default_brightness())
        except Exception as exp:
            raise exp

    def increase(self, value: int = config.brightness_step()) -> int:
        """Increase by 'value' the current brightness
        """
        try:
            new_brightness = self._apply(util.brightness_increment, value)
            return new_brightness
        except Exception as exp:
            raise exp

    def decrease(self, value: int = config.brightness_step()) -> int:
        """Decrease by 'value' the current brightness
        """
        try:
            new_brightness = self._apply(util.brightness_decrement, value)
            return new_brightness
        except Exception as exp:
            raise exp


if __name__ == "__main__":
    SINGLETON = singleton.SingleInstance()
    SERVER = zerorpc.Server(MessageHandler())
    ADDRESS = ("tcp://127.0.0.1:%s") % (config.communication_port())
    SERVER.bind(ADDRESS)
    SERVER.run()
