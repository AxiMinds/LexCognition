# lexcognition_analytics/data_analysis.py

def analyze_data(text):
    """
    Analyzes the provided text for various metrics.

    Parameters:
    text (str): The text to be analyzed.

    Returns:
    dict: A dictionary containing analysis results.
    """
    # Sentence count
    sentence_count = len(text.split('.'))
    
    # Word count
    word_count = len(text.split())
    
    # Average word length
    avg_word_length = sum(len(word) for word in text.split()) / word_count if word_count > 0 else 0
    
    # Vocabulary diversity (unique words)
    unique_words = set(text.split())
    vocab_diversity = len(unique_words) / word_count if word_count > 0 else 0
    
    # Average sentence length (in words)
    avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
    
    # Creating the result dictionary
    analysis_results = {
        'sentence_count': sentence_count,
        'word_count': word_count,
        'avg_word_length': avg_word_length,
        'vocab_diversity': vocab_diversity,
        'avg_sentence_length': avg_sentence_length
    }
    
    return analysis_results

def summarize_analysis(analysis_results):
    """
    Generates a summary based on the analysis results.

    Parameters:
    analysis_results (dict): The dictionary containing analysis results.

    Returns:
    str: A summary of the analysis.
    """
    summary = (
        f"Text Analysis Summary:\n"
        f"---------------------\n"
        f"Sentence Count: {analysis_results['sentence_count']}\n"
        f"Word Count: {analysis_results['word_count']}\n"
        f"Average Word Length: {analysis_results['avg_word_length']:.2f} characters\n"
        f"Vocabulary Diversity: {analysis_results['vocab_diversity']:.2f}\n"
        f"Average Sentence Length: {analysis_results['avg_sentence_length']:.2f} words\n"
    )
    
    return summary
