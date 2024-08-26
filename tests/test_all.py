import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your modules after setting the path
import unittest
from lexprivacy.document_processing import preprocess_documents
from lexprivacy.lexprint_generation import generate_lexprint
from lexprivacy.lexprint_application import rewrite_text_to_match_lexprint
from lexdetect.detection_algorithm import detect_human_vs_ai
from stylemorph.style_blending import blend_styles
from stylemorph.text_generation_integration import transition_style_across_text
from lexguard.signature_analysis import analyze_signature, compare_signatures
from lexguard.alert_system import check_for_impersonation
from lexaudit.version_control import track_changes, save_version_control
from lexaudit.change_analysis import analyze_changes, load_version_control
from lexaudit.audit_report_generation import generate_audit_report
from lexcognition_analytics.data_analysis import analyze_word_usage, analyze_cognitive_patterns
from lexcognition_analytics.visualization import plot_word_usage, plot_cognitive_patterns

class TestLexCognition(unittest.TestCase):

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

        self.assertEqual(len(preprocessed_docs), 3)
        self.assertIsInstance(lexprint, dict)
        self.assertGreater(len(final_text), 0)

    def test_lexdetect(self):
        sample_text = "This is a simple example text that might be written by a human or AI."
        detection_result = detect_human_vs_ai(sample_text)

        self.assertIn('is_human', detection_result)
        self.assertIn('score', detection_result)
        self.assertIsInstance(detection_result['score'], float)

    def test_stylemorph(self):
        style1 = {'avg_word_length': 4.5, 'word_count_variance': 100}
        style2 = {'avg_word_length': 5.0, 'word_count_variance': 120}
        blended_style = blend_styles(style1, style2, blend_ratio=0.3)
        sample_text = "This is a simple example text for style morphing."
        final_text = transition_style_across_text(sample_text, style1, style2, transition_points=[])

        self.assertIsInstance(blended_style, dict)
        self.assertGreater(len(final_text), 0)

    def test_lexguard(self):
        base_text = "This is the base text for signature analysis."
        new_text = "This is a new text that might deviate slightly."
        base_signature = analyze_signature(base_text)
        new_signature = analyze_signature(new_text)
        deviation = compare_signatures(base_signature, new_signature)
        alert_result = check_for_impersonation(base_signature, new_signature)

        self.assertIsInstance(alert_result, dict)
        self.assertIn('alert', alert_result)
        self.assertTrue(alert_result['alert'])

    def test_lexaudit(self):
        original_text = "This is the original text. It will be modified."
        revised_text = "This is the modified text. It has been changed."
        diff = track_changes(original_text, revised_text)
        save_version_control(diff, filename="test_version_control.json")
        diff_loaded = load_version_control(filename="test_version_control.json")
        analysis = analyze_changes(diff_loaded)
        report = generate_audit_report(filename="test_version_control.json")

        self.assertIn('additions', analysis)
        self.assertIn('deletions', analysis)
        self.assertGreater(len(report), 0)

    def test_lexcognition_analytics(self):
        sample_text = "This is a sample text to analyze word usage and cognitive patterns. It includes several sentences."
        word_usage = analyze_word_usage(sample_text)
        cognitive_patterns = analyze_cognitive_patterns(sample_text)

        self.assertIsInstance(word_usage, dict)
        self.assertIsInstance(cognitive_patterns, dict)
        self.assertGreater(len(word_usage['word_count']), 0)
        self.assertGreater(len(cognitive_patterns['sentence_lengths']), 0)

        # Visualizations - in a real test, you would not check visual output like this
        plot_word_usage(word_usage)
        plot_cognitive_patterns(cognitive_patterns)

if __name__ == '__main__':
    unittest.main()
