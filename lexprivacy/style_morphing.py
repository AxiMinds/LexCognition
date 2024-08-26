# lexprivacy/style_morphing.py

def apply_style_morphing(text, style_parameters):
    """
    Applies style morphing to the provided text based on the given style parameters.

    Parameters:
    text (str): The text to which style morphing will be applied.
    style_parameters (dict): A dictionary containing style parameters for morphing.

    Returns:
    str: The text after applying style morphing.
    """
    # Example of simple style morphing based on a few parameters
    if style_parameters.get('uppercase'):
        text = text.upper()
    if style_parameters.get('capitalize'):
        text = text.capitalize()
    if style_parameters.get('reverse'):
        text = text[::-1]
    
    # Add more style morphing logic here as needed

    return text

def summarize_style_changes(original_text, morphed_text):
    """
    Summarizes the changes between the original and morphed text.

    Parameters:
    original_text (str): The original text before style morphing.
    morphed_text (str): The text after style morphing.

    Returns:
    str: A summary of the changes made.
    """
    summary = (
        f"Original Text: {original_text}\n"
        f"Morphed Text: {morphed_text}\n"
    )
    
    return summary
