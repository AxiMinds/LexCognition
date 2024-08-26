from collections import Counter

def detect_human_vs_ai(text):
    words = text.split()
    word_count = Counter(words)
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    # Simple heuristic for demonstration (can be replaced with a more complex model)
    if avg_word_length > 4.5 and len(word_count) > 50:
        return {
            'is_human': True,
            'score': avg_word_length * len(word_count) / 100
        }
    else:
        return {
            'is_human': False,
            'score': avg_word_length * len(word_count) / 100
        }
