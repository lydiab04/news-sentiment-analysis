import unittest
import pandas as pd
from src.indicators import compute_sma

class TestIndicators(unittest.TestCase):

    def test_sma_output_length(self):
        prices = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

        sma = compute_sma(prices)

        self.assertEqual(len(sma), len(prices))

if __name__ == "__main__":
    unittest.main()