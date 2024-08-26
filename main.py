# main.py

from lexdetect.lexdetect import detect_text
from lexguard.signature_analysis import analyze_signature
from lexprivacy.style_morphing import analyze_style

def process_text(text):
    detection_results = detect_text(text)
    signature_results = analyze_signature(text)
    style_results = analyze_style(text)

    print("Text Analysis Summary:")
    print(f"Authorship Likelihood: {detection_results['summary']}")
    print(f"Language Complexity: {signature_results['summary']['language_complexity']}")
    print(f"Vocabulary Diversity: {signature_results['summary']['vocabulary_diversity']}")
    print(f"Word Usage Variation: {style_results['summary']}")

    print("\nDetailed Metrics:")
    print(f"Human Authorship Score: {detection_results['score']:.2f}")
    print(f"Average Word Length: {signature_results['avg_word_length']:.2f}")
    print(f"Unique Word Ratio: {signature_results['unique_word_ratio']:.2f}")
    print(f"Word Count Variance: {style_results['word_count_variance']:.2f}")

# Example usage
text = "Your text to analyze goes here."
process_text(text)
