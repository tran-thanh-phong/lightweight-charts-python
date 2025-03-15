import os
import pandas as pd

from lightweight_charts import Chart


def calculate_sma(df, period: int = 50):
    return pd.DataFrame(
        {"time": df["date"], f"SMA {period}": df["close"].rolling(window=period).mean()}
    ).dropna()


def calculate_macd(df, short_period=12, long_period=26, signal_period=9):
    short_ema = df["close"].ewm(span=short_period, adjust=False).mean()
    long_ema = df["close"].ewm(span=long_period, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    histogram = macd - signal
    return pd.DataFrame(
        {
            "time": df["date"],
            "MACD": macd,
            "Signal": signal,
            "Histogram": histogram,
        }
    ).dropna()


if __name__ == "__main__":
    chart = Chart(inner_height=1)
    chart.legend(visible=True)

    chart.watermark("Main")

    path = os.path.join(os.path.dirname(__file__), "ohlcv.csv")

    df = pd.read_csv(path)

    df = df.head(10)

    chart.set(df)

    sma_data = calculate_sma(df, period=5)

    line = chart.create_line("SMA 5")
    line.set(sma_data)

    # Subchart with MACD

    macd_data = calculate_macd(df)

    histogram = chart.create_histogram("MACD", pane_index=1)
    histogram.set(macd_data[["time", "MACD", "Signal", "Histogram"]])

    chart.show(block=True)
