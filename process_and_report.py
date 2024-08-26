import os
from lexdetect.analyze_text import analyze_text, output_metadata
from lexcognition_analytics.data_analysis import analyze_data
from lexprivacy.style_morphing import apply_style_morphing
from lexaudit.audit_report_generation import generate_audit_report

def process_text(text, filename):
    """
    Process the input text by performing various analyses and generating reports.

    :param text: The text to be analyzed.
    :param filename: The filename associated with the text for version control analysis.
    :return: None
    """
    print(f"Processing text from {filename}...")

    # Step 1: Perform authorship detection
    authorship_info = analyze_text(text)
    print("Authorship Detection:", authorship_info)

    # Step 2: Perform language complexity analysis
    language_info = output_metadata(text)
    print("Language Complexity Analysis:", language_info)

    # Step 3: Perform vocabulary diversity analysis
    vocabulary_info = analyze_data(text)
    print("Vocabulary Diversity Analysis:", vocabulary_info)

    # Combine the analysis results
    combined_results = {
        "authorship_info": authorship_info,
        "language_info": language_info,
        "vocabulary_info": vocabulary_info
    }
    print("Combined Analysis Results:", combined_results)

    # Step 4: Apply style morphing (if applicable)
    style_morphed_text = apply_style_morphing(text, style_parameters={})
    print("Style-Morphed Text:", style_morphed_text)

    # Step 5: Generate audit report based on version control
    audit_report = generate_audit_report(os.path.join("test_data", filename))
    if audit_report:
        print("Audit Report:", audit_report)
    else:
        print(f"No version control data found for '{filename}'.")

def main():
    """
    Main function to execute the text processing and reporting workflow.

    :return: None
    """
    # Directory containing the test data files
    test_data_dir = "test_data"

    # Loop through all text files in the test data directory
    for filename in os.listdir(test_data_dir):
        if filename.endswith('.txt'):  # Process only .txt files
            with open(os.path.join(test_data_dir, filename), 'r') as file:
                text = file.read()
                process_text(text, filename)

if __name__ == "__main__":
    main()
