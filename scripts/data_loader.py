import pandas as pd

def load_news_data(file_path):
    """Loads financial news data from a CSV file."""
    news_df = pd.read_csv(file_path)
    news_df['date'] = pd.to_datetime(news_df['date'], errors='coerce')
    return news_df

import pandas as pd

def load_stock_data(file_path):
    """Loads stock data from a CSV file."""
    stock_df = pd.read_csv(file_path)
    stock_df['Date'] = pd.to_datetime(stock_df['Date'], errors='coerce')
    stock_df.rename(columns={'Date': 'date'}, inplace=True)
    return stock_df
