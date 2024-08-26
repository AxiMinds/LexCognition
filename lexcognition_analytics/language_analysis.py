# language_analysis.py

def analyze_language_complexity(text):
    """
    Analyzes the language complexity of the input text.
    
    Parameters:
    - text (str): The input text to analyze.
    
    Returns:
    - dict: Contains average word length and language complexity summary.
    """
    avg_word_length = calculate_avg_word_length(text)
    
    summary = {
        "avg_word_length": avg_word_length,
        "language_complexity": classify_language_complexity(avg_word_length)
    }
    
    return summary

def calculate_avg_word_length(text):
    """
    Calculates the average word length of the text.
    
    Parameters:
    - text (str): The input text to analyze.
    
    Returns:
    - float: The average word length.
    """
    words = text.split()
    avg_length = sum(len(word) for word in words) / len(words)
    return avg_length

def classify_language_complexity(avg_word_length):
    """
    Classifies the language complexity based on the average word length.
    
    Parameters:
    - avg_word_length (float): The average word length.
    
    Returns:
    - str: The classification of language complexity.
    """
    if avg_word_length < 4:
        return "Simple Language"
    elif 4 <= avg_word_length < 5:
        return "Moderately Complex Language"
    else:
        return "Complex Language"
