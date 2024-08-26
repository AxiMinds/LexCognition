# analyze_text.py
import random

def analyze_text(text):
    """
    Analyzes the text to detect authorship and provides a summary.

    :param text: The text to be analyzed.
    :return: A dictionary with authorship information.
    """
    # Simulating some basic authorship detection
    score = round(random.uniform(0.8, 1.0), 2)  # Random score between 0.8 and 1.0
    is_ai_generated = score > 0.85  # Assume AI-generated if score > 0.85
    summary = f"Highly Likely AI-Generated (Score: {score})" if is_ai_generated else f"Possibly Human-Generated (Score: {score})"

    return {
        "score": score,
        "is_ai_generated": is_ai_generated,
        "summary": summary
    }

def output_metadata(text):
    """
    Outputs metadata about the text, including language complexity and vocabulary diversity.

    :param text: The text to be analyzed.
    :return: A dictionary with metadata information.
    """
    words = text.split()
    word_lengths = [len(word) for word in words]
    avg_word_length = sum(word_lengths) / len(word_lengths)

    # Simulating language complexity and vocabulary diversity
    language_complexity = "Complex Language" if avg_word_length > 5 else "Simple Language"
    unique_word_ratio = len(set(words)) / len(words)
    vocabulary_diversity = "High Diversity" if unique_word_ratio > 0.75 else "Moderate Diversity"

    return {
        "authorship_info": analyze_text(text),  # Including the authorship info in the metadata
        "language_info": {
            "avg_word_length": avg_word_length,
            "language_complexity": language_complexity,
        },
        "vocabulary_info": {
            "unique_word_ratio": unique_word_ratio,
            "vocabulary_diversity": vocabulary_diversity
        }
    }
