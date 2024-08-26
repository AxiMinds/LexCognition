import unittest
from lexprivacy.document_processing import preprocess_documents
from lexprivacy.lexprint_generation import generate_lexprint
from lexprivacy.lexprint_application import rewrite_text_to_match_lexprint

class TestLexPrivacy(unittest.TestCase):

    def test_lexprivacy(self):
        sample_docs = [
            "This is the first sample document. It has a unique writing style.",
            "Here is another sample. This document has a different style and tone.",
            "This document serves as the third example. Its style is distinct from the others."
        ]
        
        preprocessed_docs = preprocess_documents(sample_docs)
        lexprint = generate_lexprint(preprocessed_docs)
        sample_text = "This is a sample text to demonstrate rewriting."
        final_text = rewrite_text_to_match_lexprint(sample_text, lexprint)

        # Use assertions to validate the output
        self.assertEqual(len(preprocessed_docs), 3)
        self.assertIsInstance(lexprint, dict)
        self.assertGreater(len(final_text), 0)

if __name__ == '__main__':
    unittest.main()
