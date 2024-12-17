import pandas as pd
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_stock_data(file_path):
    """
    Load stock price data from a CSV file.

    Parameters:
        file_path (str): Path to the stock price CSV file.

    Returns:
        pd.DataFrame: Loaded stock data with 'Date' as a datetime column.
    """
    if not os.path.isfile(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Load data from CSV
        df = pd.read_csv(file_path)
        if df.empty:
            logging.warning(f"The file '{file_path}' is empty.")
            return pd.DataFrame()

        # Ensure 'Date' column exists and convert to datetime
        if 'Date' not in df.columns:
            raise ValueError("The file does not contain a 'Date' column.")
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Check for invalid dates
        invalid_dates = df['Date'].isna().sum()
        if invalid_dates > 0:
            logging.warning(f"{invalid_dates} invalid date(s) found and will be removed.")
            df.dropna(subset=['Date'], inplace=True)

        logging.info(f"File '{file_path}' loaded successfully.")
        return df

    except Exception as e:
        logging.error(f"Error loading file '{file_path}': {e}")
        raise

def prepare_stock_data(df):
    """
    Prepare and validate stock data for analysis.

    Parameters:
        df (pd.DataFrame): Input stock price DataFrame.

    Returns:
        pd.DataFrame: Processed stock price DataFrame with 'Date' as index.
    """
    try:
        # Define required columns
        required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        missing_columns = set(required_columns) - set(df.columns)

        # Validate required columns
        if missing_columns:
            raise ValueError(f"Missing required column(s): {missing_columns}")

        # Filter and prepare data
        df = df[required_columns].copy()  # Ensures no unintended side effects
        df.set_index('Date', inplace=True)
        df.sort_index(inplace=True)

        logging.info("Stock data prepared successfully.")
        return df

    except Exception as e:
        logging.error(f"Error preparing stock data: {e}")
        raise
