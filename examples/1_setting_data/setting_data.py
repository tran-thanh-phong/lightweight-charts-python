import pandas as pd
from lightweight_charts import Chart
import os

if __name__ == "__main__":
    chart = Chart()

    path = os.path.join(os.path.dirname(__file__), "ohlcv.csv")

    # Columns: time | open | high | low | close | volume
    df = pd.read_csv(path)
    chart.set(df)

    chart.show(block=True)
