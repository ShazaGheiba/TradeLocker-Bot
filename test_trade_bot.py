import unittest
import pandas as pd
from trade_bot import moving_average_crossover_strategy, bollinger_bands_strategy, mean_reversion_strategy, breakout_strategy

class TestTradeBot(unittest.TestCase):
    def setUp(self):
        # Sample data
        self.data = pd.DataFrame({
            'close': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
            'high': [105, 115, 125, 135, 145, 155, 165, 175, 185, 195],
            'low': [95, 105, 115, 125, 135, 145, 155, 165, 175, 185]
        })

    def test_moving_average_crossover_strategy(self):
        short_window = 3
        long_window = 7
        result = moving_average_crossover_strategy(self.data, short_window, long_window)
        # Check if columns are added
        self.assertIn('short_ma', result.columns)
        self.assertIn('long_ma', result.columns)
        self.assertIn('signal', result.columns)
        # Check for correct signal generation
        self.assertEqual(list(result['signal']), [0, 0, 0, 0, 0, 0, 1, 1, 1, 1])

    def test_bollinger_bands_strategy(self):
        window = 5
        num_std = 2
        result = bollinger_bands_strategy(self.data, window, num_std)
        # Check if columns are added
        self.assertIn('rolling_mean', result.columns)
        self.assertIn('rolling_std', result.columns)
        self.assertIn('upper_band', result.columns)
        self.assertIn('lower_band', result.columns)
        self.assertIn('signal', result.columns)
        # Check for correct signal generation
        self.assertEqual(list(result['signal']), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_mean_reversion_strategy(self):
        window = 5
        num_std = 1
        result = mean_reversion_strategy(self.data, window, num_std)
        # Check if columns are added
        self.assertIn('rolling_mean', result.columns)
        self.assertIn('rolling_std', result.columns)
        self.assertIn('upper_bound', result.columns)
        self.assertIn('lower_bound', result.columns)
        self.assertIn('signal', result.columns)
        # Check for correct signal generation
        self.assertEqual(list(result['signal']), [0, 0, 0, 0, -1, -1, -1, -1, -1, -1])

    def test_breakout_strategy(self):
        window = 5
        result = breakout_strategy(self.data, window)
        # Check if columns are added
        self.assertIn('rolling_high', result.columns)
        self.assertIn('rolling_low', result.columns)
        self.assertIn('signal', result.columns)
        # Check for correct signal generation
        self.assertEqual(list(result['signal']), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
