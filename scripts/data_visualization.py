import matplotlib.pyplot as plt
import seaborn as sns

def calculate_technical_indicators(df):
    """Calculate SMA and RSI indicators."""
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()

    # Calculate Relative Strength Index (RSI)
    delta = df['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    return df


def plot_stock_data(df):
    """Visualize stock prices with technical indicators."""
    plt.figure(figsize=(14, 7))

    plt.plot(df.index, df['Close'], label='Close Price', color='blue')
    plt.plot(df.index, df['SMA_50'], label='50-day SMA', color='orange')
    plt.plot(df.index, df['SMA_200'], label='200-day SMA', color='green')
    plt.title('Stock Price with SMA Indicators')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

def plot_rsi(df):
    """Plot Relative Strength Index (RSI)."""
    plt.figure(figsize=(14, 5))
    plt.plot(df.index, df['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('Relative Strength Index (RSI)')
    plt.grid(True)
    plt.show()
