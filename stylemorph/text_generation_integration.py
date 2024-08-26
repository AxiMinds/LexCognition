from stylemorph.style_blending import blend_styles

def apply_style_to_text(text, blended_style):
    words = text.split()
    avg_word_length = blended_style['avg_word_length']
    
    styled_text = []
    for word in words:
        if len(word) < avg_word_length:
            styled_text.append(word.upper())  # Example transformation
        else:
            styled_text.append(word.lower())
    
    return ' '.join(styled_text)

def transition_style_across_text(text, style1, style2, transition_points):
    blended_style = blend_styles(style1, style2, blend_ratio=0.5)
    return apply_style_to_text(text, blended_style)

if __name__ == "__main__":
    text = "This is a simple example text for style morphing."
    style1 = {'avg_word_length': 4.5, 'word_count_variance': 100}
    style2 = {'avg_word_length': 5.0, 'word_count_variance': 120}
    
    final_text = transition_style_across_text(text, style1, style2, transition_points=[])
    print("Styled Text:", final_text)
