import unittest
from lexdetect.detection_algorithm import detect_human_vs_ai

class TestLexDetect(unittest.TestCase):

    def test_lexdetect(self):
        sample_text = "This is a simple example text that might be written by a human or AI."
        detection_result = detect_human_vs_ai(sample_text)
        
        print("Sample Text:", sample_text)
        print("Detection Result:", detection_result)
        
        # Example assertions
        self.assertIn('is_human', detection_result)
        self.assertIn('score', detection_result)
        self.assertIsInstance(detection_result['score'], float)

if __name__ == '__main__':
    unittest.main()
