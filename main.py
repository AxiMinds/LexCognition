# main.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from lexdetect import detect_text
    from lexguard import analyze_signature
    from lexprivacy import analyze_style, morph_style
    from lexaudit import generate_audit_report
    from lexvisualize import visualize_analysis
    from lexsentiment import analyze_sentiment
except ImportError as e:
    print(f"Error: Required module not found. {str(e)}")
    print("Please ensure all required directories are in the same parent directory as main.py.")
    sys.exit(1)

def process_text(text, previous_version=None):
    """
    Analyze the given text using various linguistic analysis tools.
    
    Args:
    text (str): The input text to analyze.
    previous_version (dict): The previous version of the text for change tracking.
    
    Returns:
    None: Prints analysis results to console.
    """
    try:
        detection_results = detect_text(text)
        signature_results = analyze_signature(text)
        style_results = analyze_style(text)
        morphed_text = morph_style(text, "formal")  # Example target style
        sentiment_results = analyze_sentiment(text)
        audit_report = generate_audit_report(text, {"source": "user_input"}, previous_version)

        print("Text Analysis Summary:")
        print(f"Authorship Likelihood: {detection_results['summary']}")
        print(f"Language Complexity: {signature_results['summary']['language_complexity']}")
        print(f"Vocabulary Diversity: {signature_results['summary']['vocabulary_diversity']}")
        print(f"Word Usage Variation: {style_results['summary']}")
        print(f"Sentiment: {sentiment_results['sentiment']} (Polarity: {sentiment_results['polarity']:.2f}, Subjectivity: {sentiment_results['subjectivity']:.2f})")

        print("\nDetailed Metrics:")
        print(f"Human Authorship Score: {detection_results['score']:.2f}")
        print(f"Average Word Length: {signature_results['avg_word_length']:.2f}")
        print(f"Unique Word Ratio: {signature_results['unique_word_ratio']:.2f}")
        print(f"Word Count Variance: {style_results['word_count_variance']:.2f}")

        print("\nStyle Morphing:")
        print(f"Original Text: {text}")
        print(f"Morphed Text (Formal Style): {morphed_text}")

        print("\nAudit Report:")
        print(audit_report)

        # Generate and save visualizations
        visualizations = visualize_analysis(audit_report)
        print("\nVisualizations:")
        for key, img_base64 in visualizations.items():
            print(f"{key}: A base64 encoded image has been generated. Length: {len(img_base64)} characters")

    except Exception as e:
        print(f"An error occurred during text processing: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to analyze: ")
    process_text(text)# main.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from lexdetect import detect_text
    from lexguard import analyze_signature
    from lexprivacy import analyze_style, morph_style
    from lexaudit import generate_audit_report
    from lexvisualize import visualize_analysis
    from lexsentiment import analyze_sentiment
    from lexnlp.nlp_processor import NLPProcessor
except ImportError as e:
    print(f"Error: Required module not found. {str(e)}")
    print("Please ensure all required directories are in the same parent directory as main.py.")
    sys.exit(1)

def process_text(text, previous_version=None):
    """
    Analyze the given text using various linguistic analysis tools.
    
    Args:
    text (str): The input text to analyze.
    previous_version (dict): The previous version of the text for change tracking.
    
    Returns:
    None: Prints analysis results to console.
    """
    try:
        detection_results = detect_text(text)
        signature_results = analyze_signature(text)
        style_results = analyze_style(text)
        morphed_text = morph_style(text, "formal")  # Example target style
        sentiment_results = analyze_sentiment(text)
        audit_report = generate_audit_report(text, {"source": "user_input"}, previous_version)

        # New NLP processing
        nlp_processor = NLPProcessor()
        pos_tagging = nlp_processor.process_text(text, "Perform part-of-speech tagging on this text.", api='ollama', model='codellama')
        named_entities = nlp_processor.process_text(text, "Identify named entities in this text.", api='openai')
        summary = nlp_processor.process_text(text, "Provide a brief summary of this text.", api='anthropic')

        print("Text Analysis Summary:")
        print(f"Authorship Likelihood: {detection_results['summary']}")
        print(f"Language Complexity: {signature_results['summary']['language_complexity']}")
        print(f"Vocabulary Diversity: {signature_results['summary']['vocabulary_diversity']}")
        print(f"Word Usage Variation: {style_results['summary']}")
        print(f"Sentiment: {sentiment_results['sentiment']} (Polarity: {sentiment_results['polarity']:.2f}, Subjectivity: {sentiment_results['subjectivity']:.2f})")

        print("\nDetailed Metrics:")
        print(f"Human Authorship Score: {detection_results['score']:.2f}")
        print(f"Average Word Length: {signature_results['avg_word_length']:.2f}")
        print(f"Unique Word Ratio: {signature_results['unique_word_ratio']:.2f}")
        print(f"Word Count Variance: {style_results['word_count_variance']:.2f}")

        print("\nStyle Morphing:")
        print(f"Original Text: {text}")
        print(f"Morphed Text (Formal Style): {morphed_text}")

        print("\nAudit Report:")
        print(audit_report)

        print("\nAdvanced NLP Analysis:")
        print(f"Part-of-Speech Tagging: {pos_tagging}")
        print(f"Named Entities: {named_entities}")
        print(f"Summary: {summary}")

        # Generate and save visualizations
        visualizations = visualize_analysis(audit_report)
        print("\nVisualizations:")
        for key, img_base64 in visualizations.items():
            print(f"{key}: A base64 encoded image has been generated. Length: {len(img_base64)} characters")

    except Exception as e:
        print(f"An error occurred during text processing: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to analyze: ")
    process_text(text)# main.py

import sys
import os

# Add the parent directory to sys.path to allow importing from subdirectories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from lexdetect import detect_text
    from lexguard import analyze_signature
    from lexprivacy import analyze_style
except ImportError as e:
    print(f"Error: Required module not found. {str(e)}")
    print("Please ensure lexdetect, lexguard, and lexprivacy directories are in the same parent directory as main.py.")
    sys.exit(1)

def process_text(text):
    """
    Analyze the given text using various linguistic analysis tools.
    
    Args:
    text (str): The input text to analyze.
    
    Returns:
    None: Prints analysis results to console.
    """
    try:
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
    except Exception as e:
        print(f"An error occurred during text processing: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to analyze: ")
    process_text(text)# main.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from lexdetect import detect_text
    from lexguard import analyze_signature
    from lexprivacy import analyze_style, morph_style
    from lexaudit import generate_audit_report
    from lexvisualize import visualize_analysis
except ImportError as e:
    print(f"Error: Required module not found. {str(e)}")
    print("Please ensure all required directories are in the same parent directory as main.py.")
    sys.exit(1)

def process_text(text):
    """
    Analyze the given text using various linguistic analysis tools.
    
    Args:
    text (str): The input text to analyze.
    
    Returns:
    None: Prints analysis results to console.
    """
    try:
        detection_results = detect_text(text)
        signature_results = analyze_signature(text)
        style_results = analyze_style(text)
        morphed_text = morph_style(text, "formal")  # Example target style
        audit_report = generate_audit_report(text, {"source": "user_input"})

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

        print("\nStyle Morphing:")
        print(f"Original Text: {text}")
        print(f"Morphed Text (Formal Style): {morphed_text}")

        print("\nAudit Report:")
        print(audit_report)

        # Generate and save visualization
        vis_data = {
            "text_stats": {
                "word_count": audit_report["text_stats"]["word_count"],
                "character_count": audit_report["text_stats"]["character_count"]
            }
        }
        img_base64 = visualize_analysis(vis_data)
        print("\nVisualization:")
        print(f"A base64 encoded image has been generated. Length: {len(img_base64)} characters")
        print("You can decode and view this image using appropriate tools or libraries.")

    except Exception as e:
        print(f"An error occurred during text processing: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to analyze: ")
    process_text(text)# main.py

import sys
import os

# Add the parent directory to sys.path to allow importing from subdirectories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from lexdetect import detect_text
    from lexguard import analyze_signature
    from lexprivacy import analyze_style
except ImportError as e:
    print(f"Error: Required module not found. {str(e)}")
    print("Please ensure lexdetect, lexguard, and lexprivacy directories are in the same parent directory as main.py.")
    sys.exit(1)

def process_text(text):
    """
    Analyze the given text using various linguistic analysis tools.
    
    Args:
    text (str): The input text to analyze.
    
    Returns:
    None: Prints analysis results to console.
    """
    try:
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
    except Exception as e:
        print(f"An error occurred during text processing: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to analyze: ")
    process_text(text)# main.py

import sys
import os

# Add the parent directory to sys.path to allow importing from subdirectories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from lexdetect import detect_text
    from lexguard import analyze_signature
    from lexprivacy import analyze_style
except ImportError as e:
    print(f"Error: Required module not found. {str(e)}")
    print("Please ensure lexdetect, lexguard, and lexprivacy directories are in the same parent directory as main.py.")
    sys.exit(1)

def process_text(text):
    """
    Analyze the given text using various linguistic analysis tools.
    
    Args:
    text (str): The input text to analyze.
    
    Returns:
    None: Prints analysis results to console.
    """
    try:
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
    except Exception as e:
        print(f"An error occurred during text processing: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to analyze: ")
    process_text(text)# main.py

try:
    from lexdetect.lexdetect import detect_text
    from lexguard.signature_analysis import analyze_signature
    from lexprivacy.style_morphing import analyze_style
except ImportError:
    print("Error: Required modules not found. Please install lexdetect, lexguard, and lexprivacy.")
    exit(1)

def process_text(text):
    """
    Analyze the given text using various linguistic analysis tools.
    
    Args:
    text (str): The input text to analyze.
    
    Returns:
    None: Prints analysis results to console.
    """
    try:
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
    except Exception as e:
        print(f"An error occurred during text processing: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to analyze: ")
    process_text(text)# main.py

import sys
import os

# Add the parent directory to sys.path to allow importing from subdirectories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from lexdetect import detect_text
    from lexguard import analyze_signature
    from lexprivacy import analyze_style
except ImportError as e:
    print(f"Error: Required module not found. {str(e)}")
    print("Please ensure lexdetect, lexguard, and lexprivacy directories are in the same parent directory as main.py.")
    sys.exit(1)

def process_text(text):
    """
    Analyze the given text using various linguistic analysis tools.
    
    Args:
    text (str): The input text to analyze.
    
    Returns:
    None: Prints analysis results to console.
    """
    try:
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
    except Exception as e:
        print(f"An error occurred during text processing: {str(e)}")

if __name__ == "__main__":
    text = input("Enter the text you want to analyze: ")
    process_text(text)# main.py

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
process_text(text)# main.py

from lexdetect.lexdetect import detect_text
from lexguard.signature_analysis import analyze_signature
from lexprivacy.style_morphing import analyze_style

# ... rest of the code remains the samefrom lexdetect.lexdetect import detect_text
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
text = "This is a sample text for analysis. It contains multiple sentences with varying structure and vocabulary to demonstrate the capabilities of our text analysis tools."
process_text(text)
