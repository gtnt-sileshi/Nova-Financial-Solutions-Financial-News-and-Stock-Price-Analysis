from textblob import TextBlob
import pandas as pd

def calculate_correlation(news_df, stock_df):
    # Step 1: Normalize and align dates
    news_df['date'] = pd.to_datetime(news_df['date']).dt.date
    stock_df['date'] = pd.to_datetime(stock_df['date']).dt.date

    # Merge news and stock data on 'date'
    combined_df = news_df.merge(stock_df[['date', 'Close']], on='date', how='inner')

    # Step 2: Conduct Sentiment Analysis on news headlines
    # Using TextBlob to assign sentiment scores to headlines
    combined_df['sentiment'] = combined_df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Drop rows with missing values
    combined_df.dropna(subset=['Close', 'sentiment'], inplace=True)

    # Step 3: Calculate Daily Stock Returns
    combined_df['daily_return'] = combined_df['Close'].pct_change()

    # Calculate the correlation between sentiment and daily returns
    correlation_df = combined_df[['sentiment', 'daily_return']].corr()

    return combined_df['sentiment'], combined_df['daily_return'], correlation_df