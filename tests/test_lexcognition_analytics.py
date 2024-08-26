from lexcognition_analytics.data_analysis import analyze_word_usage, analyze_cognitive_patterns
from lexcognition_analytics.visualization import plot_word_usage, plot_cognitive_patterns

def test_lexcognition_analytics():
    sample_text = "This is a sample text to analyze word usage and cognitive patterns. It includes several sentences."
    
    # Analyze word usage and cognitive patterns
    word_usage = analyze_word_usage(sample_text)
    cognitive_patterns = analyze_cognitive_patterns(sample_text)
    
    # Output results
    print("Test LexCognition Analytics Module:")
    print("Word Usage Analysis:", word_usage)
    print("Cognitive Pattern Analysis:", cognitive_patterns)
    
    # Visualize results
    plot_word_usage(word_usage)
    plot_cognitive_patterns(cognitive_patterns)

test_lexcognition_analytics()
