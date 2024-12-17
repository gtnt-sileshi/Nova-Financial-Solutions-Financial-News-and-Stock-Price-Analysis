import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def publisher_analysis(df, publisher_col):
    """
    Analyze and visualize the most frequent publishers.

    Parameters:
        df (pd.DataFrame): Input DataFrame containing publisher data.
        publisher_col (str): Column name containing publisher information.

    Returns:
        pd.Series: Frequency count of publishers.
    """
    try:
        if publisher_col not in df.columns:
            raise ValueError(f"Column '{publisher_col}' not found in the DataFrame.")

        # Handle missing or empty values
        df = df.dropna(subset=[publisher_col])
        if df.empty:
            raise ValueError("The publisher column contains only missing values.")

        # Count occurrences of publishers
        publisher_counts = df[publisher_col].value_counts()

        # Plot top 10 publishers
        plt.figure(figsize=(10, 6))
        sns.barplot(y=publisher_counts.index[:10], x=publisher_counts.values[:10], orient='h', palette="coolwarm")
        plt.title('Top Publishers', fontsize=14)
        plt.xlabel('Number of Articles', fontsize=12)
        plt.ylabel('Publisher', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

        logging.info("Publisher analysis completed successfully.")
        return publisher_counts

    except Exception as e:
        logging.error(f"Error in publisher analysis: {e}")
        raise


def extract_domains(df, publisher_col):
    """
    Extract and count unique domains from publisher email addresses.

    Parameters:
        df (pd.DataFrame): Input DataFrame containing publisher email addresses.
        publisher_col (str): Column name containing email addresses.

    Returns:
        pd.Series: Frequency count of unique domains.
    """
    try:
        if publisher_col not in df.columns:
            raise ValueError(f"Column '{publisher_col}' not found in the DataFrame.")

        # Handle missing values and invalid entries
        df = df.dropna(subset=[publisher_col])
        if df.empty:
            raise ValueError("The publisher column contains only missing values.")

        # Extract domain names using regex
        def extract_domain(email):
            match = re.search(r'@([\w\.-]+)', str(email))
            return match.group(1) if match else None

        df['domain'] = df[publisher_col].apply(extract_domain)

        # Handle cases with no valid domains
        if df['domain'].isna().all():
            raise ValueError("No valid email domains found in the data.")

        # Count domain occurrences
        domain_counts = df['domain'].value_counts()

        # Plot top 10 domains
        plt.figure(figsize=(10, 6))
        sns.barplot(y=domain_counts.index[:10], x=domain_counts.values[:10], orient='h', palette="mako")
        plt.title('Top Email Domains', fontsize=14)
        plt.xlabel('Number of Articles', fontsize=12)
        plt.ylabel('Domain', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

        logging.info("Domain extraction and analysis completed successfully.")
        return domain_counts

    except Exception as e:
        logging.error(f"Error in domain extraction: {e}")
        raise
