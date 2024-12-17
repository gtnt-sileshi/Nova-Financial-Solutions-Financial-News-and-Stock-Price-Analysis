import matplotlib.pyplot as plt

def plot_correlation(sentiment_scores, daily_returns):
    """
    Plots sentiment scores against stock returns for correlation visualization.

    Args:
        sentiment_scores (pd.Series or list): Sentiment scores.
        daily_returns (pd.Series or list): Corresponding daily stock returns.

    Returns:
        None
    """
    # Error handling to check input lengths
    if len(sentiment_scores) != len(daily_returns):
        raise ValueError("Sentiment scores and daily returns must be of the same length.")

    plt.figure(figsize=(10, 6))
    plt.scatter(sentiment_scores, daily_returns, alpha=0.7, c='b', edgecolor='k', marker='o')
    plt.title("Correlation Between Sentiment Scores and Stock Returns")
    plt.xlabel("Sentiment Scores")
    plt.ylabel("Daily Stock Returns")
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Optionally, display a line of best fit (regression line)
    if len(sentiment_scores) > 1:
        # Fit a linear regression line to the scatter plot
        from numpy import polyfit
        coefficients = polyfit(sentiment_scores, daily_returns, 1)
        plt.plot(sentiment_scores, coefficients[0] * sentiment_scores + coefficients[1], color='r', linestyle='--', label=f'Fit: y={coefficients[0]:.2f}x + {coefficients[1]:.2f}')
        plt.legend(loc='best')

    plt.tight_layout()
    plt.show()
