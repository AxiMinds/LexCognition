import numpy as np

def blend_styles(style1, style2, blend_ratio=0.5):
    blended_style = {
        'avg_word_length': np.average([style1['avg_word_length'], style2['avg_word_length']], 
                                      weights=[blend_ratio, 1-blend_ratio]),
        'word_count_variance': np.average([style1['word_count_variance'], style2['word_count_variance']], 
                                           weights=[blend_ratio, 1-blend_ratio]),
    }
    return blended_style
