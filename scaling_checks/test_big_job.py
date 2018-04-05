import chepstow
import random
import time
import unittest


class BigTest(unittest.TestCase):
    def test_something(self):
        # randomly fails for testing purposes
        agent = chepstow.Agent()
        delay = random.randint(0, 10)
        start = time.time()
        agent.run(delay)
        stop = time.time()
        total = stop - start
        self.assertLess(total, 7, "The something test now takes {} seconds".format(total))
