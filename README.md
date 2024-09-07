# LexCognition

## Overview

LexCognition is a comprehensive AI-based text analysis tool that performs multiple analyses on text files. The system can detect authorship, analyze language complexity, assess vocabulary diversity, perform style morphing, and generate audit reports.

## Features

- Authorship Detection
- Language Complexity Analysis
- Vocabulary Diversity Analysis
- Style Morphing
- Audit Reporting
- Sentiment Analysis (Coming Soon)
- Visualization Tools (Coming Soon)

## Directory Structure

```plaintext
.
├── main.py
├── lexdetect/
│   └── __init__.py
├── lexguard/
│   └── __init__.py
├── lexprivacy/
│   └── __init__.py
├── lexaudit/
│   └── __init__.py
├── lexvisualize/
│   └── __init__.py
├── tests/
│   └── test_main.py
├── README.md
└── ROADMAP.md# LexCognition

## Overview

LexCognition is a comprehensive AI-based text analysis tool that performs multiple analyses on text files. The system can detect authorship, analyze language complexity, assess vocabulary diversity, perform style morphing, and generate audit reports.

## Features

- Authorship Detection
- Language Complexity Analysis
- Vocabulary Diversity Analysis
- Style Morphing
- Audit Reporting
- Sentiment Analysis (Coming Soon)
- Visualization Tools (Coming Soon)

## Directory Structure

```plaintext
.
├── main.py
├── lexdetect/
│   └── __init__.py
├── lexguard/
│   └── __init__.py
├── lexprivacy/
│   └── __init__.py
├── lexaudit/
│   └── __init__.py
├── lexvisualize/
│   └── __init__.py
├── tests/
│   └── test_main.py
├── README.md
└── ROADMAP.md# LexCognition

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
├── main.py
├── lexdetect/
│   └── __init__.py
├── lexguard/
│   └── __init__.py
├── lexprivacy/
│   └── __init__.py
├── lexaudit/
│   └── __init__.py
├── lexvisualize/
│   └── __init__.py
├── tests/
│   └── test_main.py
├── README.md
└── ROADMAP.md
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

## API Documentation

lexdetect
- detect_text(text: str) -> dict: Determines the likelihood of AI-generated text.

lexguard
- analyze_signature(text: str) -> dict: Analyzes language complexity and vocabulary diversity.

lexprivacy
- analyze_style(text: str) -> dict: Assesses word usage variation.
- morph_style(text: str, target_style: str) -> str: Transforms text into a specified style.

lexaudit
- generate_audit_report(text: str, metadata: dict) -> dict: Generates a comprehensive audit report.

lexvisualize (Coming Soon)
- Will provide visualization tools for text analysis results.

Testing
Run the test suite:
```shell
python -m unittest discover tests
```
## Contributing

We welcome contributions to LexCognition! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for more information on how to get involved.

## Roadmap

For information about upcoming features and long-term goals, please see our [ROADMAP.md](ROADMAP.md).

## Changelog

### Version 0.1.0
- Initial release
- Basic text analysis pipeline
- Authorship detection
- Language complexity analysis
- Vocabulary diversity analysis
- Basic style morphing

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions, suggestions, or issues, please open an issue in this repository or contact [your email].
