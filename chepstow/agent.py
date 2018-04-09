import time


class Agent(object):
    """Base Agent class

    This class does nothing, but demonstrates style for code and docstrings.

    Attributes:
        magic (int): Use this attribute when you need some magic.
    """

    def __init__(self):
        self.magic = 762

    def run(self, delay):
        """Run the agent

        Args:
            delay (float): number of seconds to delay before running
        """
        time.sleep(delay)
