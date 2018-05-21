#! /usr/bin/env python3

import zerorpc


class MessageHandler(object):
    """This is the mane message handler to handle message
    received by clients
    """

    def reset(self) -> int:
        """Reset to default value the brightness of the monitor
        """
        return 10

    # TODO put the value int inside a variable read from a config file
    def increase(self, value: int = 10) -> int:
        """Increase by 'value' the current brightness
        """
        return value

    # TODO put the value int inside a variable read from a config file
    def decrease(self, value: int = 10) -> int:
        """Decrease by 'value' the current brightness
        """
        return value


if __name__ == "__main__":
    SERVER = zerorpc.Server(MessageHandler())
    SERVER.bind("tcp://127.0.0.1:9999") # TODO: put the port inside configs
    SERVER.run()
