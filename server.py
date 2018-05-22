#! /usr/bin/env python3

"""This is the main file for the server part of the native brightness
controller. It aims to provide a communication interface suitable to
let client control the brightness without tempering with file permission
on the brightness system file.

This file should be run as root if you want it to work properly.
"""


#  import configparser
import zerorpc

import config
import util


last_change = util.timestamp()


class MessageHandler(object):
    """This is the mane message handler to handle message
    received by clients
    """

    @staticmethod
    def reset() -> int:
        """Reset to default value the brightness of the monitor
        """
        return 10

    @staticmethod
    def increase(value: int = config.brightness_step()) -> int:
        """Increase by 'value' the current brightness
        """
        return value

    @staticmethod
    def decrease(value: int = config.brightness_step()) -> int:
        """Decrease by 'value' the current brightness
        """
        return value


if __name__ == "__main__":
    SERVER = zerorpc.Server(MessageHandler())
    ADDRESS = ("tcp://127.0.0.1:%s") % (config.communication_port())
    SERVER.bind(ADDRESS)
    SERVER.run()
