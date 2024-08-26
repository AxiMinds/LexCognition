# lexdetect/lexdetect.py

def detect_text(text):
    """
    Detect if the given text is human-written or AI-generated.

    Parameters:
    text (str or list): The text to be analyzed. Can be a single string or a list of strings.

    Returns:
    dict: A dictionary containing a boolean 'is_human', a 'score' indicating the likelihood,
          and a 'summary' with a simplified explanation for clarity.
    """

    if isinstance(text, list):
        text = ' '.join(text)  # Join list into a single string

    word_count = len(text.split())
    avg_word_length = sum(len(word) for word in text.split()) / word_count if word_count > 0 else 0

    is_human = avg_word_length < 5.5  # This threshold is arbitrary for demonstration
    score = avg_word_length / 10

    # Simplified explanation
    if score < 0.3:
        summary = "Highly Likely AI-Generated"
    elif score < 0.5:
        summary = "Possible AI-Generated"
    elif score < 0.7:
        summary = "Likely Human-Generated"
    else:
        summary = "Highly Likely Human-Generated"

    return {
        "is_human": is_human,
        "score": score,
        "summary": f"{summary} (Score: {score:.2f})"
    }
