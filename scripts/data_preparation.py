import pandas as pd

def load_stock_data(file_path):
    """Load stock price data from a CSV file."""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def prepare_stock_data(df):
    """Ensure data contains essential columns for analysis."""
    required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    df = df[required_columns]
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    return df
