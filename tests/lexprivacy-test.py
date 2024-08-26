from collections import Counter
import numpy as np

# Sample documents to simulate different writing styles
sample_docs = [
    "This is the first sample document. It has a unique writing style.",
    "Here is another sample. This document has a different style and tone.",
    "This document serves as the third example. Its style is distinct from the others."
]

# Function to preprocess documents
def preprocess_documents(documents):
    preprocessed_docs = []
    for doc in documents:
        preprocessed_doc = ' '.join(doc.split())  # Basic preprocessing
        preprocessed_docs.append(preprocessed_doc)
    return preprocessed_docs

# Preprocessing the sample documents
preprocessed_docs = preprocess_documents(sample_docs)

# Function to generate LexPrint
def analyze_writing_style(documents):
    word_counts = Counter()
    for doc in documents:
        word_counts.update(doc.split())
    return word_counts

def generate_lexprint(documents):
    preprocessed_docs = preprocess_documents(documents)
    style_analysis = analyze_writing_style(preprocessed_docs)
    avg_word_length = np.mean([len(word) for word in style_analysis])
    return {
        'word_counts': style_analysis,
        'avg_word_length': avg_word_length,
    }

# Generating LexPrint from the preprocessed documents
lexprint = generate_lexprint(preprocessed_docs)

# Function to apply LexPrint to new text
def rewrite_text_to_match_lexprint(text, lexprint):
    words = text.split()
    lexprint_avg_word_length = lexprint['avg_word_length']
    
    rewritten_text = []
    for word in words:
        if len(word) < lexprint_avg_word_length:
            rewritten_text.append(word.upper())  # Example transformation
        else:
            rewritten_text.append(word.lower())
    
    return ' '.join(rewritten_text)

# Sample text to apply the generated LexPrint
sample_text = "This is a sample text to demonstrate rewriting."
final_text = rewrite_text_to_match_lexprint(sample_text, lexprint)

# Output the results
print("Preprocessed Documents:", preprocessed_docs)
print("Generated LexPrint:", lexprint)
print("Final Text with Applied LexPrint:", final_text)
