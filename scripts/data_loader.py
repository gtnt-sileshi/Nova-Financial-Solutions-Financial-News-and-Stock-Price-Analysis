import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_csv_data(file_path, required_columns=None, date_column=None):
    """
    General function to load a CSV file into a DataFrame with validation.

    Parameters:
        file_path (str): Path to the CSV file.
        required_columns (list): List of columns required in the CSV.
        date_column (str): Column name containing date values for conversion.

    Returns:
        pd.DataFrame: Loaded and validated DataFrame.
    """
    if not os.path.isfile(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            logging.warning(f"The file '{file_path}' is empty.")
            return pd.DataFrame()
        
        # Validate required columns
        if required_columns and not set(required_columns).issubset(df.columns):
            missing_cols = set(required_columns) - set(df.columns)
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        # Convert date column to datetime
        if date_column:
            df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
            invalid_dates = df[date_column].isna().sum()
            if invalid_dates > 0:
                logging.warning(f"{invalid_dates} invalid dates found in column '{date_column}'.")
        
        logging.info(f"File '{file_path}' loaded successfully.")
        return df

    except Exception as e:
        logging.error(f"Error loading file '{file_path}': {e}")
        raise

def load_news_data(file_path):
    """
    Loads financial news data from a CSV file.

    Parameters:
        file_path (str): Path to the financial news CSV file.

    Returns:
        pd.DataFrame: News DataFrame with 'date' column in datetime format.
    """
    return load_csv_data(file_path, required_columns=['date', 'headline'], date_column='date')

def load_stock_data(file_path):
    """
    Loads stock market data from a CSV file.

    Parameters:
        file_path (str): Path to the stock data CSV file.

    Returns:
        pd.DataFrame: Stock DataFrame with 'date' column in datetime format.
    """
    df = load_csv_data(file_path, required_columns=['Date', 'Close'], date_column='Date')
    df.rename(columns={'Date': 'date'}, inplace=True)
    return df
