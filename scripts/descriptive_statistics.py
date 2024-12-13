import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def basic_statistics(df, column):
    """Calculate basic statistics for a text column."""
    df['text_length'] = df[column].apply(len)
    return df['text_length'].describe()

def articles_per_publisher(df, publisher_col):
    """Count the number of articles per publisher and display top 10."""
    publisher_counts = df[publisher_col].value_counts().nlargest(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=publisher_counts.index, y=publisher_counts.values)
    plt.xticks(rotation=45, ha='right')
    plt.title('Top 10 Publishers by Number of Articles')
    plt.ylabel('Number of Articles')
    plt.xlabel('Publisher')
    plt.tight_layout()
    plt.show()
    return publisher_counts


def publication_trends(df, date_col):
    """Analyze the publication trends over time."""
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df['year_month'] = df[date_col].dt.to_period('M')
    trends = df.groupby('year_month').size()
    plt.figure(figsize=(12, 6))
    trends.plot(kind='line', marker='o', color='b')
    plt.title('Publication Trends Over Time')
    plt.ylabel('Number of Articles')
    plt.xlabel('Month')
    plt.grid()
    plt.show()
    return trends
