import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_technical_indicators(df):
    """
    Calculate Simple Moving Averages (SMA) and Relative Strength Index (RSI) indicators.

    Parameters:
        df (pd.DataFrame): Input DataFrame containing 'Close' column.

    Returns:
        pd.DataFrame: DataFrame with added 'SMA_50', 'SMA_200', and 'RSI' columns.
    """
    try:
        if 'Close' not in df.columns:
            raise ValueError("The input DataFrame must contain a 'Close' column.")

        # Calculate Simple Moving Averages
        df['SMA_50'] = df['Close'].rolling(window=50, min_periods=1).mean()
        df['SMA_200'] = df['Close'].rolling(window=200, min_periods=1).mean()

        # Calculate Relative Strength Index (RSI)
        delta = df['Close'].diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=14, min_periods=1).mean()
        avg_loss = loss.rolling(window=14, min_periods=1).mean()

        # Prevent division by zero
        rs = avg_gain / avg_loss.replace(0, float('inf'))
        df['RSI'] = 100 - (100 / (1 + rs))

        logging.info("Technical indicators (SMA and RSI) calculated successfully.")
        return df

    except Exception as e:
        logging.error(f"Error in calculating technical indicators: {e}")
        raise


def plot_stock_data(df):
    """
    Plot stock closing prices with Simple Moving Averages (SMA).

    Parameters:
        df (pd.DataFrame): Input DataFrame containing 'Close', 'SMA_50', and 'SMA_200' columns.
    """
    try:
        if not {'Close', 'SMA_50', 'SMA_200'}.issubset(df.columns):
            raise ValueError("The DataFrame must contain 'Close', 'SMA_50', and 'SMA_200' columns.")

        plt.figure(figsize=(14, 7))
        sns.set_style("whitegrid")

        plt.plot(df.index, df['Close'], label='Close Price', color='blue', linewidth=1.5)
        plt.plot(df.index, df['SMA_50'], label='50-Day SMA', color='orange', linestyle='--', linewidth=1.5)
        plt.plot(df.index, df['SMA_200'], label='200-Day SMA', color='green', linestyle='--', linewidth=1.5)

        plt.title('Stock Price with SMA Indicators', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Price', fontsize=12)
        plt.legend(loc='best', fontsize=10)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        logging.error(f"Error in plotting stock data: {e}")
        raise


def plot_rsi(df):
    """
    Plot Relative Strength Index (RSI) with overbought and oversold levels.

    Parameters:
        df (pd.DataFrame): Input DataFrame containing 'RSI' column.
    """
    try:
        if 'RSI' not in df.columns:
            raise ValueError("The DataFrame must contain an 'RSI' column.")

        plt.figure(figsize=(14, 5))
        sns.set_style("whitegrid")

        plt.plot(df.index, df['RSI'], label='RSI', color='purple', linewidth=1.5)
        plt.axhline(70, color='red', linestyle='--', linewidth=1, label='Overbought (70)')
        plt.axhline(30, color='green', linestyle='--', linewidth=1, label='Oversold (30)')

        plt.title('Relative Strength Index (RSI)', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('RSI', fontsize=12)
        plt.legend(loc='best', fontsize=10)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        logging.error(f"Error in plotting RSI: {e}")
        raise
