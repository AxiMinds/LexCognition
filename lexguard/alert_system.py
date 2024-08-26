from lexguard.signature_analysis import compare_signatures

def check_for_impersonation(base_signature, new_signature, threshold=0.1):
    deviation = compare_signatures(base_signature, new_signature)
    
    # Basic alert condition based on deviation thresholds
    if deviation['avg_word_length_diff'] > threshold or deviation['unique_word_ratio_diff'] > threshold:
        return {
            'alert': True,
            'message': 'Possible impersonation detected!',
            'deviation': deviation
        }
    else:
        return {
            'alert': False,
            'message': 'No significant deviation detected.',
            'deviation': deviation
        }

if __name__ == "__main__":
    base_signature = {'avg_word_length': 4.5, 'unique_word_ratio': 0.6, 'word_count': 100}
    new_signature = {'avg_word_length': 5.0, 'unique_word_ratio': 0.7, 'word_count': 95}

    alert_result = check_for_impersonation(base_signature, new_signature)
    print(alert_result)
