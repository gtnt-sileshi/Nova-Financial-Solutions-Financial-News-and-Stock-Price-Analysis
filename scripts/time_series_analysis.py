import matplotlib.pyplot as plt
import pandas as pd

def publication_frequency(df, date_col):
    """
    Analyze and visualize publication frequency over time.

    Args:
        df (pd.DataFrame): Input DataFrame containing the date column.
        date_col (str): Column name containing date information.

    Returns:
        pd.Series: Publication frequency grouped by date.
    """
    if date_col not in df.columns:
        raise ValueError(f"Column '{date_col}' does not exist in the DataFrame.")

    # Ensure the date column is in datetime format
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    # Drop rows with invalid dates
    df = df.dropna(subset=[date_col])

    # Group by publication date
    frequency = df.groupby(df[date_col].dt.date).size()

    # Plot publication frequency
    plt.figure(figsize=(12, 6))
    plt.plot(frequency.index, frequency.values, marker='o', color='purple', linestyle='-')
    plt.title('Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    return frequency


def publishing_times_analysis(df, date_col):
    """
    Analyze and visualize publishing times to identify hourly trends.

    Args:
        df (pd.DataFrame): Input DataFrame containing the date column.
        date_col (str): Column name containing datetime information.

    Returns:
        pd.Series: Hourly publication counts.
    """
    if date_col not in df.columns:
        raise ValueError(f"Column '{date_col}' does not exist in the DataFrame.")

    # Ensure the date column is in datetime format
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    # Drop rows with invalid dates
    df = df.dropna(subset=[date_col])

    # Extract publishing hour and calculate hourly counts
    df['hour'] = df[date_col].dt.hour
    hourly_counts = df['hour'].value_counts().sort_index()

    # Plot hourly publishing trends
    plt.figure(figsize=(10, 6))
    plt.bar(hourly_counts.index, hourly_counts.values, color='orange', width=0.8)
    plt.title('Publishing Times Analysis')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Articles')
    plt.xticks(range(0, 24))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    return hourly_counts
