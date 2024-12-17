import pandas as pd
import talib

def calculate_technical_indicators(df):
    """
    Calculate basic technical indicators using TA-Lib.

    Parameters:
        df (pd.DataFrame): Input DataFrame containing a 'Close' column for stock prices.

    Returns:
        pd.DataFrame: DataFrame with added SMA (50, 200), RSI, and MACD indicators.
    """
    try:
        # Check if 'Close' column exists
        if 'Close' not in df.columns:
            raise ValueError("The input DataFrame must contain a 'Close' column for calculations.")

        # Handle missing or non-numeric 'Close' data
        if not pd.api.types.is_numeric_dtype(df['Close']):
            raise ValueError("The 'Close' column must contain numeric values.")
        
        # Drop rows with NaN values in 'Close' to avoid computation issues
        df = df.dropna(subset=['Close']).copy()

        # Calculate indicators using TA-Lib
        df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
        df['SMA_200'] = talib.SMA(df['Close'], timeperiod=200)
        df['RSI'] = talib.RSI(df['Close'], timeperiod=14)

        macd, macd_signal, macd_hist = talib.MACD(
            df['Close'], fastperiod=12, slowperiod=26, signalperiod=9
        )
        df['MACD'] = macd
        df['MACD_Signal'] = macd_signal
        df['MACD_Hist'] = macd_hist

        return df

    except Exception as e:
        print(f"Error calculating technical indicators: {e}")
        raise
