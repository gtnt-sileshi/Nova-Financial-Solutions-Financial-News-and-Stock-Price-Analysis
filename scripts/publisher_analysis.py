import re
import matplotlib.pyplot as plt
import seaborn as sns

def publisher_analysis(df, publisher_col):
    """Analyze the most frequent publishers."""
    publisher_counts = df[publisher_col].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(y=publisher_counts.index[:10], x=publisher_counts.values[:10], orient='h')
    plt.title('Top Publishers')
    plt.xlabel('Number of Articles')
    plt.ylabel('Publisher')
    plt.show()
    return publisher_counts

def extract_domains(df, publisher_col):
    """Extract and count unique domains from publisher emails."""
    df['domain'] = df[publisher_col].apply(lambda x: re.search(r'@([\w.]+)', x).group(1) if '@' in x else None)
    domain_counts = df['domain'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(y=domain_counts.index[:10], x=domain_counts.values[:10], orient='h')
    plt.title('Top Email Domains')
    plt.xlabel('Number of Articles')
    plt.ylabel('Domain')
    plt.show()
    return domain_counts
