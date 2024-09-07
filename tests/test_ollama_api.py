# tests/test_ollama_api.py

import unittest
from unittest.mock import patch, MagicMock
from lexnlp.ollama_api import OllamaAPI

class TestOllamaAPI(unittest.TestCase):
    @patch('lexnlp.ollama_api.requests.post')
    def test_generate_text(self, mock_post):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {'response': 'Mocked response'}
        mock_post.return_value = mock_response

        ollama = OllamaAPI()
        result = ollama.generate_text("Test prompt")

        self.assertEqual(result, 'Mocked response')
        mock_post.assert_called_once()

    def test_invalid_model(self):
        ollama = OllamaAPI()
        with self.assertRaises(ValueError):
            ollama.generate_text("Test prompt", model_name="invalid_model")

if __name__ == '__main__':
    unittest.main()