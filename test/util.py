import unittest
import pandas as pd
import os

from lightweight_charts import Chart

path = os.path.join(os.path.dirname(__file__), "../examples/1_setting_data/ohlcv.csv")

BARS = pd.read_csv(path)


class Tester(unittest.TestCase):
    def setUp(self):
        self.chart: Chart = Chart(100, 100, 800, 100)

    def tearDown(self) -> None:
        self.chart.exit()
