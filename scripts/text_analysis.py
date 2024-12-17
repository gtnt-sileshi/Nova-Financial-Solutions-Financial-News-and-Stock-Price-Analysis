from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import nltk

# Download resources if not already downloaded
nltk.download('vader_lexicon', quiet=True)


def sentiment_analysis(df, text_col):
    """
    Perform sentiment analysis on a text column using NLTK's SentimentIntensityAnalyzer.
    Adds sentiment scores to the dataframe and visualizes the sentiment distribution.

    Args:
        df (pd.DataFrame): Input dataframe containing the text column.
        text_col (str): Name of the column containing text data.

    Returns:
        pd.DataFrame: DataFrame with an additional 'sentiment' column.
    """
    if text_col not in df.columns:
        raise ValueError(f"Column '{text_col}' does not exist in the DataFrame.")

    sia = SentimentIntensityAnalyzer()

    # Apply sentiment analysis, handle missing or non-string data
    df['sentiment'] = df[text_col].apply(lambda x: 
                                        sia.polarity_scores(str(x))['compound'] 
                                        if pd.notna(x) else 0)

    # Sentiment Bins: Negative [-1, -0.5), Neutral [-0.5, 0.5), Positive [0.5, 1]
    bins = [-1.1, -0.5, 0.5, 1.1]
    labels = ['Negative', 'Neutral', 'Positive']
    df['sentiment_label'] = pd.cut(df['sentiment'], bins=bins, labels=labels, include_lowest=True)

    # Plot sentiment distribution
    sentiment_counts = df['sentiment_label'].value_counts()
    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind='bar', color=['red', 'gray', 'green'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    return df


def generate_wordcloud(df, text_col, stopwords=None):
    """
    Generate and display a word cloud from a text column.

    Args:
        df (pd.DataFrame): Input dataframe containing the text column.
        text_col (str): Name of the column containing text data.
        stopwords (set): Custom stopwords to exclude from the word cloud.

    Returns:
        None
    """
    if text_col not in df.columns:
        raise ValueError(f"Column '{text_col}' does not exist in the DataFrame.")

    # Aggregate all text data into a single string
    text = ' '.join(str(x) for x in df[text_col].dropna())

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, 
                          background_color='black',
                          stopwords=stopwords, 
                          collocations=False).generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Headlines')
    plt.tight_layout()
    plt.show()
