# vocabulary_analysis.py

def analyze_vocabulary_diversity(text):
    """
    Analyzes the vocabulary diversity of the input text.
    
    Parameters:
    - text (str): The input text to analyze.
    
    Returns:
    - dict: Contains unique word ratio and vocabulary diversity summary.
    """
    unique_word_ratio = calculate_unique_word_ratio(text)
    
    summary = {
        "unique_word_ratio": unique_word_ratio,
        "vocabulary_diversity": classify_vocabulary_diversity(unique_word_ratio)
    }
    
    return summary

def calculate_unique_word_ratio(text):
    """
    Calculates the ratio of unique words in the text.
    
    Parameters:
    - text (str): The input text to analyze.
    
    Returns:
    - float: The unique word ratio.
    """
    words = text.split()
    unique_words = set(words)
    return len(unique_words) / len(words)

def classify_vocabulary_diversity(unique_word_ratio):
    """
    Classifies the vocabulary diversity based on the unique word ratio.
    
    Parameters:
    - unique_word_ratio (float): The unique word ratio.
    
    Returns:
    - str: The classification of vocabulary diversity.
    """
    if unique_word_ratio < 0.5:
        return "Low Diversity"
    elif 0.5 <= unique_word_ratio < 0.75:
        return "Moderate Diversity"
    else:
        return "High Diversity"

