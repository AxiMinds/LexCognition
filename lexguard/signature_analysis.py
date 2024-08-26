# lexguard/signature_analysis.py

def analyze_signature(text):
    """
    Analyze the signature of the text to determine key characteristics.

    Parameters:
    text (str or list): The text to be analyzed. Can be a single string or a list of strings.

    Returns:
    dict: A dictionary containing average word length, unique word ratio, word count, and simplified summaries.
    """

    if isinstance(text, list):
        text = ' '.join(text)  # Join list into a single string

    words = text.split()
    word_count = len(words)
    unique_words = set(words)

    avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
    unique_word_ratio = len(unique_words) / word_count if word_count > 0 else 0

    # Simplified explanations
    if avg_word_length < 3.0:
        language_complexity = "Simple Language"
    elif avg_word_length < 5.0:
        language_complexity = "Moderately Complex Language"
    elif avg_word_length < 7.0:
        language_complexity = "Complex Language"
    else:
        language_complexity = "Highly Complex Language"

    if unique_word_ratio < 0.3:
        vocabulary_diversity = "Low Diversity"
    elif unique_word_ratio < 0.6:
        vocabulary_diversity = "Moderate Diversity"
    elif unique_word_ratio < 0.8:
        vocabulary_diversity = "High Diversity"
    else:
        vocabulary_diversity = "Very High Diversity"

    return {
        "avg_word_length": avg_word_length,
        "unique_word_ratio": unique_word_ratio,
        "word_count": word_count,
        "summary": {
            "language_complexity": f"{language_complexity} (Average Word Length: {avg_word_length:.2f})",
            "vocabulary_diversity": f"{vocabulary_diversity} (Unique Word Ratio: {unique_word_ratio:.2f})"
        }
    }
