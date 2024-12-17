import matplotlib.pyplot as plt

def plot_correlation(sentiment_scores, daily_returns):
    """Plots sentiment scores and stock returns for correlation visualization."""
    plt.figure(figsize=(10, 6))
    plt.scatter(sentiment_scores, daily_returns, alpha=0.7)
    plt.title("Correlation Between Sentiment and Stock Returns")
    plt.xlabel("Average Daily Sentiment Score")
    plt.ylabel("Average Daily Stock Return")
    plt.grid()
    plt.show()