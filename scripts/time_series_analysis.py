import matplotlib.pyplot as plt
import pandas as pd

def publication_frequency(df, date_col):
    """Analyze publication frequency over time."""
    df[date_col] = pd.to_datetime(df[date_col])
    frequency = df.groupby(df[date_col].dt.date).size()
    plt.figure(figsize=(12, 6))
    frequency.plot(kind='line', marker='o', color='purple')
    plt.title('Publication Frequency Over Time')
    plt.ylabel('Number of Articles')
    plt.xlabel('Date')
    plt.grid()
    plt.show()
    return frequency

def publishing_times_analysis(df, date_col):
    """Analyze publishing times to identify trends."""
    df['hour'] = pd.to_datetime(df[date_col]).dt.hour
    hourly_counts = df['hour'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    hourly_counts.plot(kind='bar', color='orange')
    plt.title('Publishing Times Analysis')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Articles')
    plt.grid()
    plt.show()
    return hourly_counts
