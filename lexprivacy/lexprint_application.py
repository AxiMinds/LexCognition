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
