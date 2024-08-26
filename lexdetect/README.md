# Text Analysis Suite

## Overview
The Text Analysis Suite is a collection of Python modules designed to analyze text for various linguistic attributes. This suite provides insights into the complexity, diversity, and authorship likelihood of a given text.

## Features
- **Authorship Detection:** Detects the likelihood of a text being AI-generated based on specific algorithms.
- **Language Complexity Analysis:** Evaluates the complexity of the language used in the text by calculating average word length.
- **Vocabulary Diversity Analysis:** Measures the diversity of the vocabulary by calculating the unique word ratio.

## Directory Structure
- `authorship_detection.py`: Detects AI authorship likelihood
- `language_analysis.py`: Analyzes language complexity
- `vocabulary_analysis.py`: Analyzes vocabulary diversity
- `analyze_text.py`: Integrates all analysis modules
- `README.md`: Documentation for the suite

## Usage

### Authorship Detection
To detect whether a text is likely AI-generated:

```python
from authorship_detection import detect_authorship

text = "Your input text here"
authorship_info = detect_authorship(text)
print(authorship_info)
```

### Language Complexity Analysis
To analyze the language complexity of a text:

```python
from language_analysis import analyze_language_complexity

text = "Your input text here"
language_info = analyze_language_complexity(text)
print(language_info)
```

### Vocabulary Diversity Analysis
To analyze the vocabulary diversity of a text:

```python
from vocabulary_analysis import analyze_vocabulary_diversity

text = "Your input text here"
vocabulary_info = analyze_vocabulary_diversity(text)
print(vocabulary_info)
```

### Combined Analysis
To perform a combined analysis of authorship, language complexity, and vocabulary diversity:

```python
from analyze_text import analyze_text, output_metadata

text = "Your input text here"
analysis_results = analyze_text(text)
output_metadata(analysis_results)
```

## Installation

Clone the repository and navigate to the directory:

```bash
git clone https://github.com/your-repo-url/text-analysis-suite.git
cd text-analysis-suite
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

---

This should now display correctly without formatting issues related to Markdown code blocks.
