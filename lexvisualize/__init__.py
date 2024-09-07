# lexvisualize/__init__.py

import matplotlib.pyplot as plt
from io import BytesIO
import base64

def visualize_analysis(analysis_results: dict) -> dict:
    """
    Create visualizations for text analysis results.

    Args:
    analysis_results (dict): The results of text analysis.

    Returns:
    dict: A dictionary containing base64 encoded strings of the visualization images.
    """
    visualizations = {}

    # Text statistics bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(['Words', 'Characters'], 
            [analysis_results['text_stats']['word_count'], 
             analysis_results['text_stats']['character_count']])
    plt.title('Text Statistics')
    plt.ylabel('Count')
    visualizations['text_stats'] = _get_image_base64()

    # If we have change data, create a change visualization
    if 'changes' in analysis_results:
        plt.figure(figsize=(10, 5))
        changes = analysis_results['changes']
        plt.bar(['Word Count', 'Character Count', 'Avg Word Length'], 
                [changes['word_count_change'], changes['char_count_change'], changes['avg_word_length_change']])
        plt.title('Changes from Previous Version')
        plt.ylabel('Change')
        visualizations['changes'] = _get_image_base64()

    return visualizations

def _get_image_base64():
    """Helper function to get base64 encoded image"""
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
    plt.close()
    return img_base64# lexvisualize/__init__.py

import matplotlib.pyplot as plt
from io import BytesIO
import base64

def visualize_analysis(analysis_results: dict) -> str:
    """
    Create visualizations for text analysis results.

    Args:
    analysis_results (dict): The results of text analysis.

    Returns:
    str: A base64 encoded string of the visualization image.
    """
    # Create a simple bar chart of word counts
    plt.figure(figsize=(10, 5))
    plt.bar(['Words', 'Characters'], 
            [analysis_results['text_stats']['word_count'], 
             analysis_results['text_stats']['character_count']])
    plt.title('Text Statistics')
    plt.ylabel('Count')

    # Save the plot to a BytesIO object
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # Encode the image to base64
    img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to free up memory

    return img_base64
  