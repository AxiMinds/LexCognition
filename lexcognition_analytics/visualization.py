import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend suitable for headless environments

import matplotlib.pyplot as plt
import numpy as np

def plot_word_usage(word_usage):
    words, counts = zip(*word_usage['word_count'].most_common(10))
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Word Usage')
    plt.savefig('word_usage_plot.png')  # Save the plot as a file instead of displaying it
    plt.close()

def plot_cognitive_patterns(cognitive_patterns):
    sentence_lengths = cognitive_patterns['sentence_lengths']
    plt.hist(sentence_lengths, bins=range(1, max(sentence_lengths)+1))
    plt.xlabel('Sentence Length (words)')
    plt.ylabel('Frequency')
    plt.title('Sentence Length Distribution')
    plt.savefig('sentence_length_distribution.png')  # Save the plot as a file instead of displaying it
    plt.close()

if __name__ == "__main__":
    word_usage = {
        'word_count': {'This': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'to': 1, 'analyze': 1, 'word': 1, 'usage': 1},
        'avg_word_length': 4.0,
        'unique_word_ratio': 1.0,
        'total_words': 10
    }
    
    cognitive_patterns = {
        'complexity': 7.0,
        'readability': 4.5,
        'sentence_lengths': [7, 8]
    }
    
    plot_word_usage(word_usage)
    plot_cognitive_patterns(cognitive_patterns)
