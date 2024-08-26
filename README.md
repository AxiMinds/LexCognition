# LexCognition

## Overview

LexCognition is a comprehensive AI-based text analysis tool that performs multiple analyses on text files. The system can detect authorship, analyze language complexity, and assess vocabulary diversity. It also provides style-morphed text based on the input and generates detailed audit reports. This tool is useful for analyzing and processing large volumes of text to determine potential AI generation, complexity levels, and other linguistic features.

## Features

- **Authorship Detection**: Determines the likelihood that a text is AI-generated or human-written.
- **Language Complexity Analysis**: Analyzes the average word length, language complexity, and diversity of vocabulary.
- **Vocabulary Diversity Analysis**: Provides statistics on sentence count, word count, average sentence length, and more.
- **Style Morphing**: Transforms the input text into a new style while retaining its original meaning.
- **Audit Reporting**: Generates detailed reports based on text analysis and version control data.

## Directory Structure

```plaintext
.
├── analyze_text.py               # Script for analyzing text
├── lexaudit                      # Directory containing auditing tools and scripts
│   ├── audit_report_generation.py  # Script for generating audit reports
│   ├── change_analysis.py          # Script for analyzing changes
│   └── __init__.py                 # Init file for the lexaudit module
├── lexdetect                     # Directory containing authorship detection tools
├── lexguard                      # Directory for security and privacy tools
├── lexprivacy                    # Directory for privacy analysis tools
├── lexcognition_analytics        # Directory containing analytics scripts
├── process_and_report.py         # Main script to process text files and generate reports
├── reports                       # Directory where generated reports are stored
├── requirements.txt              # Python dependencies
├── test_data                     # Directory containing test text files
└── README.md                     # This file
```

## Installation

### Prerequisites

- Python 3.10 or later
- Pip (Python package manager)

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/LexCognition.git
   cd LexCognition
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Main Script

To process and analyze text files in the `test_data` directory, run the following command:

```bash
python process_and_report.py
```

This script will analyze each text file in the `test_data` directory, generate an authorship detection report, language complexity analysis, vocabulary diversity analysis, style-morphed text, and a comprehensive audit report.

### Example Output

When you run `process_and_report.py`, you'll see output similar to the following:

```plaintext
Processing text from example-file.txt...
Authorship Detection: {'score': 0.89, 'is_ai_generated': True, 'summary': 'Highly Likely AI-Generated (Score: 0.89)'}
Language Complexity Analysis: {'avg_word_length': 5.2, 'language_complexity': 'Complex Language', 'vocabulary_diversity': 'High Diversity'}
Vocabulary Diversity Analysis: {'sentence_count': 12, 'word_count': 150, 'avg_sentence_length': 12.5}
Audit Report: {'filename': 'test_data/example-file.txt', 'changes': None, 'analysis_summary': 'Analysis based on version control data'}
```

### Output Files

The audit reports and other analyses are stored in the `reports` directory. Each report is saved as a JSON or plain text file (depending on the analysis), making it easy to review and share results.

## Contributing

Contributions are welcome! Please submit a pull request with a detailed description of your changes. Ensure that your code follows the existing style and passes all tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions, suggestions, or issues, please open an issue in this repository or contact [your email].
