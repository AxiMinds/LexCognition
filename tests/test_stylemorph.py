from stylemorph.style_blending import blend_styles
from stylemorph.text_generation_integration import transition_style_across_text

def test_stylemorph():
    style1 = {'avg_word_length': 4.5, 'word_count_variance': 100}
    style2 = {'avg_word_length': 5.0, 'word_count_variance': 120}
    
    blended_style = blend_styles(style1, style2, blend_ratio=0.3)
    sample_text = "This is a simple example text for style morphing."
    final_text = transition_style_across_text(sample_text, style1, style2, transition_points=[])
    
    print("Test StyleMorph Function:")
    print("Blended Style:", blended_style)
    print("Final Text with Applied Style:", final_text)

test_stylemorph()
