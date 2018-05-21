#! /usr/bin/env python3

import zerorpc
import configparser


# config
#  CONFIG_FILE = "/opt/native-backlight/config"
CONFIG_FILE = "config"

# config - Network
CFG_NETWORK_SEC = "NETWORK"
CFG_PORT = "port"

# config - Other
CFG_OTHER_SEC = "OTHER"
CFG_THRESHOLD = "threshold"
CFG_STEP = "step"
CFG_BRIGHTNESS_FILE = "brightness_file"


CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)

# Network
PORT = CONFIG[CFG_NETWORK_SEC].getint(CFG_PORT)

# Other
THRESHOLD = CONFIG[CFG_OTHER_SEC].getint(CFG_THRESHOLD)
STEP = CONFIG[CFG_OTHER_SEC].getint(CFG_STEP)
BRIGHTNESS_FILE = CONFIG[CFG_OTHER_SEC][CFG_BRIGHTNESS_FILE]


class MessageHandler(object):
    """This is the mane message handler to handle message
    received by clients
    """

    def reset(self) -> int:
        """Reset to default value the brightness of the monitor
        """
        return 10

    def increase(self, value: int = STEP) -> int:
        """Increase by 'value' the current brightness
        """
        return value

    def decrease(self, value: int = STEP) -> int:
        """Decrease by 'value' the current brightness
        """
        return value


if __name__ == "__main__":
    SERVER = zerorpc.Server(MessageHandler())
    ADDRESS = ("tcp://127.0.0.1:%s") % (PORT)
    SERVER.bind(ADDRESS)
    SERVER.run()
