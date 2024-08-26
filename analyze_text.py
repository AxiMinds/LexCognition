# analyze_text.py

from authorship_detection import detect_authorship
from language_analysis import analyze_language_complexity
from vocabulary_analysis import analyze_vocabulary_diversity

def analyze_text(text):
    """
    Analyzes the text for authorship, language complexity, and vocabulary diversity.
    
    Parameters:
    - text (str): The input text to analyze.
    
    Returns:
    - dict: The analysis results.
    """
    authorship_info = detect_authorship(text)
    language_info = analyze_language_complexity(text)
    vocabulary_info = analyze_vocabulary_diversity(text)
    
    return {
        "authorship_info": authorship_info,
        "language_info": language_info,
        "vocabulary_info": vocabulary_info
    }

def output_metadata(analysis_results):
    """
    Outputs the combined analysis results metadata.
    
    Parameters:
    - analysis_results (dict): The combined analysis results.
    """
    print("\n--- Analysis Results ---\n")
    
    print("Authorship Detection:")
    print(f"Score: {analysis_results['authorship_info']['score']:.2f}")
    print(analysis_results['authorship_info']['summary'])
    
    print("\nLanguage Complexity:")
    print(f"Average Word Length: {analysis_results['language_info']['avg_word_length']:.2f}")
    print(analysis_results['language_info']['language_complexity'])
    
    print("\nVocabulary Diversity:")
    print(f"Unique Word Ratio: {analysis_results['vocabulary_info']['unique_word_ratio']:.2f}")
    print(analysis_results['vocabulary_info']['vocabulary_diversity'])
