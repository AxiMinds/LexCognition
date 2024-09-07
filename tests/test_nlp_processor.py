# tests/test_nlp_processor.py

import unittest
from unittest.mock import patch
from lexnlp.nlp_processor import NLPProcessor

class TestNLPProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = NLPProcessor()

    @patch('lexnlp.ollama_api.OllamaAPI.generate_text')
    def test_text_classification(self, mock_generate_text):
        mock_generate_text.return_value = "Category: Technology"
        result = self.processor.text_classification("Apple released a new iPhone", ["Technology", "Sports", "Politics"])
        self.assertEqual(result, "Category: Technology")

    @patch('lexnlp.ollama_api.OllamaAPI.generate_text')
    def test_named_entity_recognition(self, mock_generate_text):
        mock_generate_text.return_value = "Entities: Apple (Organization), iPhone (Product)"
        result = self.processor.named_entity_recognition("Apple released a new iPhone")
        self.assertEqual(result, "Entities: Apple (Organization), iPhone (Product)")

    @patch('lexnlp.ollama_api.OllamaAPI.generate_text')
    def test_sentiment_analysis(self, mock_generate_text):
        mock_generate_text.return_value = "Sentiment: Positive"
        result = self.processor.sentiment_analysis("I love this product!")
        self.assertEqual(result, "Sentiment: Positive")

if __name__ == '__main__':
    unittest.main()# tests/test_nlp_processor.py

import unittest
from unittest.mock import patch
from lexnlp.nlp_processor import NLPProcessor

class TestNLPProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = NLPProcessor()

    @patch('lexnlp.ollama_api.OllamaAPI.generate_text')
    def test_text_classification(self, mock_generate_text):
        mock_generate_text.return_value = "Category: Technology"
        result = self.processor.text_classification("Apple released a new iPhone", ["Technology", "Sports", "Politics"])
        self.assertEqual(result, "Category: Technology")

    @patch('lexnlp.ollama_api.OllamaAPI.generate_text')
    def test_named_entity_recognition(self, mock_generate_text):
        mock_generate_text.return_value = "Entities: Apple (Organization), iPhone (Product)"
        result = self.processor.named_entity_recognition("Apple released a new iPhone")
        self.assertEqual(result, "Entities: Apple (Organization), iPhone (Product)")

    @patch('lexnlp.ollama_api.OllamaAPI.generate_text')
    def test_sentiment_analysis(self, mock_generate_text):
        mock_generate_text.return_value = "Sentiment: Positive"
        result = self.processor.sentiment_analysis("I love this product!")
        self.assertEqual(result, "Sentiment: Positive")

if __name__ == '__main__':
    unittest.main()