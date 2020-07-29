from unittest import TestCase

from utilities import generate_time_series
import numpy as np


class Test(TestCase):
    def test_generate_time_series(self):
        samples = generate_time_series(5.0, 3.0, 20, only_seed=True)
        self.assertEqual(5.0, round(np.mean(samples), 5))
        self.assertEqual(3.0, round(np.std(samples), 5))
        self.assertEqual(20, len(samples))
