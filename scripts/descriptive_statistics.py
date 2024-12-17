import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def basic_statistics(df, column):
    """
    Calculate basic statistics for a text column.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        column (str): The column name containing text data.

    Returns:
        pd.Series: Basic descriptive statistics of text lengths.
    """
    try:
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in the DataFrame.")
        
        # Ensure text column has valid string values
        df[column] = df[column].fillna("").astype(str)
        df['text_length'] = df[column].apply(len)

        stats = df['text_length'].describe()
        logging.info("Basic text statistics calculated successfully.")
        return stats

    except Exception as e:
        logging.error(f"Error in calculating basic statistics: {e}")
        raise


def articles_per_publisher(df, publisher_col):
    """
    Count the number of articles per publisher and display the top 10.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        publisher_col (str): Column name containing publisher names.

    Returns:
        pd.Series: Top 10 publishers by article count.
    """
    try:
        if publisher_col not in df.columns:
            raise ValueError(f"Column '{publisher_col}' not found in the DataFrame.")

        # Calculate publisher counts
        publisher_counts = df[publisher_col].value_counts().nlargest(10)

        # Plot the results
        plt.figure(figsize=(12, 8))
        sns.barplot(x=publisher_counts.index, y=publisher_counts.values, palette="viridis")
        plt.xticks(rotation=45, ha='right')
        plt.title('Top 10 Publishers by Number of Articles', fontsize=14)
        plt.ylabel('Number of Articles', fontsize=12)
        plt.xlabel('Publisher', fontsize=12)
        plt.tight_layout()
        plt.show()

        logging.info("Top 10 publishers plotted successfully.")
        return publisher_counts

    except Exception as e:
        logging.error(f"Error in analyzing articles per publisher: {e}")
        raise


def publication_trends(df, date_col):
    """
    Analyze publication trends over time.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        date_col (str): Column name containing publication dates.

    Returns:
        pd.Series: Number of articles published per month.
    """
    try:
        if date_col not in df.columns:
            raise ValueError(f"Column '{date_col}' not found in the DataFrame.")

        # Convert dates to datetime
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        if df[date_col].isna().all():
            raise ValueError("All date values are invalid or missing after conversion.")

        # Extract year and month
        df['year_month'] = df[date_col].dt.to_period('M')

        # Group by year and month
        trends = df.groupby('year_month').size()

        # Plot the trends
        plt.figure(figsize=(12, 6))
        trends.plot(kind='line', marker='o', color='b')
        plt.title('Publication Trends Over Time', fontsize=14)
        plt.ylabel('Number of Articles', fontsize=12)
        plt.xlabel('Month', fontsize=12)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        logging.info("Publication trends analyzed successfully.")
        return trends

    except Exception as e:
        logging.error(f"Error in analyzing publication trends: {e}")
        raise
