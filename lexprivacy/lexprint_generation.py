import collections
import re

def generate_lexprint(text):
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text)
    
    print(f"Debug: Words found - {words}")
    
    # Calculate the average word length
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
    
    # Generate word counts
    word_counts = collections.Counter(words)
    
    lexprint = {
        'avg_word_length': avg_word_length,
        'word_counts': word_counts
    }
    
    return lexprint
