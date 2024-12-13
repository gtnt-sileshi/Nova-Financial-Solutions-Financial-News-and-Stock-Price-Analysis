from nltk.sentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.download('vader_lexicon')

def sentiment_analysis(df, text_col):
    """Perform sentiment analysis and add sentiment scores."""
    sia = SentimentIntensityAnalyzer()
    df['sentiment'] = df[text_col].apply(lambda x: sia.polarity_scores(x)['compound'])
    sentiment_counts = df['sentiment'].value_counts(bins=3)
    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind='bar', color=['red', 'gray', 'green'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Articles')
    plt.show()
    return df

def generate_wordcloud(df, text_col):
    """Generate a word cloud for a text column."""
    text = ' '.join(df[text_col].tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Headlines')
    plt.show()
