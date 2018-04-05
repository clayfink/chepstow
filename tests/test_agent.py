from chepstow.agent import *
import unittest


class AgentTest(unittest.TestCase):
    def test_something(self):
        agent = Agent()
        agent.run(0.1)
        self.assertIsNone(None)
