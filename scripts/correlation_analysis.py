from textblob import TextBlob
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def calculate_correlation(news_df, stock_df):
    """
    Calculates the correlation between sentiment scores of news headlines 
    and daily stock returns.

    Parameters:
        news_df (pd.DataFrame): DataFrame containing news data with 'date' and 'headline' columns.
        stock_df (pd.DataFrame): DataFrame containing stock data with 'date' and 'Close' columns.

    Returns:
        tuple: (sentiment_series, daily_return_series, correlation_df)
            - sentiment_series: Sentiment scores for news headlines.
            - daily_return_series: Calculated daily stock returns.
            - correlation_df: Correlation matrix between sentiment and daily returns.
    """
    try:
        # Validate input DataFrames
        if not isinstance(news_df, pd.DataFrame) or not isinstance(stock_df, pd.DataFrame):
            raise ValueError("Both news_df and stock_df must be pandas DataFrames.")

        # Check for required columns
        required_news_cols = {'date', 'headline'}
        required_stock_cols = {'date', 'Close'}

        if not required_news_cols.issubset(news_df.columns):
            raise ValueError(f"news_df must contain the following columns: {required_news_cols}")
        if not required_stock_cols.issubset(stock_df.columns):
            raise ValueError(f"stock_df must contain the following columns: {required_stock_cols}")

        logging.info("Input validation passed. Proceeding with processing.")

        # Step 1: Normalize and align dates
        news_df = news_df.copy()
        stock_df = stock_df.copy()
        
        try:
            news_df['date'] = pd.to_datetime(news_df['date']).dt.date
            stock_df['date'] = pd.to_datetime(stock_df['date']).dt.date
        except Exception as e:
            raise ValueError(f"Error in date conversion: {e}")

        # Merge news and stock data on 'date'
        combined_df = news_df.merge(stock_df[['date', 'Close']], on='date', how='inner')
        if combined_df.empty:
            logging.warning("Merged DataFrame is empty. Ensure the dates in both datasets overlap.")
            return pd.Series(), pd.Series(), pd.DataFrame()

        logging.info("Data merged successfully.")

        # Step 2: Sentiment Analysis on news headlines
        def calculate_sentiment(text):
            try:
                return TextBlob(text).sentiment.polarity
            except Exception as e:
                logging.error(f"Error in sentiment analysis: {e}")
                return None
        
        combined_df['sentiment'] = combined_df['headline'].apply(lambda x: calculate_sentiment(x))

        # Drop rows with missing values
        combined_df.dropna(subset=['Close', 'sentiment'], inplace=True)
        if combined_df.empty:
            logging.warning("No valid rows left after dropping missing values.")
            return pd.Series(), pd.Series(), pd.DataFrame()

        logging.info("Sentiment analysis completed and missing values handled.")

        # Step 3: Calculate Daily Stock Returns
        combined_df['daily_return'] = combined_df['Close'].pct_change()
        combined_df.dropna(subset=['daily_return'], inplace=True)  # Drop NaN returns after pct_change

        if combined_df.empty:
            logging.warning("No valid rows left after calculating daily returns.")
            return pd.Series(), pd.Series(), pd.DataFrame()

        logging.info("Daily stock returns calculated successfully.")

        # Step 4: Calculate Correlation
        correlation_df = combined_df[['sentiment', 'daily_return']].corr()

        logging.info("Correlation calculation completed.")

        # Return sentiment series, daily returns series, and correlation DataFrame
        return combined_df['sentiment'], combined_df['daily_return'], correlation_df

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return pd.Series(), pd.Series(), pd.DataFrame()
