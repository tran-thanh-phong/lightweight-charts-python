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
    chart = Chart(inner_height=0.7)
    chart.legend(visible=True)

    chart2 = chart.create_subchart(position="left", width=1, height=0.3)

    chart.watermark("Main")
    chart2.watermark("Sub")

    df = pd.read_csv("ohlcv.csv")
    chart.set(df)

    line = chart.create_line("SMA 50")
    sma_data = calculate_sma(df, period=50)
    line.set(sma_data)

    # Subchart with MACD
    # chart2.set(df)

    macd_data = calculate_macd(df)
    histogram = chart2.create_histogram("MACD")
    histogram.set(macd_data[["time", "MACD", "Signal", "Histogram"]])

    # line2 = chart2.create_line("SMA 50")
    # line2.set(sma_data)

    chart.show(block=True)
