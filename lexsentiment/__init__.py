# lexsentiment/__init__.py

from textblob import TextBlob

def analyze_sentiment(text: str) -> dict:
    """
    Perform sentiment analysis on the given text.

    Args:
    text (str): The input text to analyze.

    Returns:
    dict: A dictionary containing sentiment analysis results.
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment

    # Convert polarity to a descriptive label
    if sentiment.polarity > 0.1:
        sentiment_label = "Positive"
    elif sentiment.polarity < -0.1:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity,
        "sentiment": sentiment_label
    }