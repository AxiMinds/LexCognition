from lexguard.signature_analysis import analyze_signature, compare_signatures
from lexguard.alert_system import check_for_impersonation

def test_lexguard():
    base_text = "This is the base text for signature analysis."
    new_text = "This is a new text that might deviate slightly."
    
    base_signature = analyze_signature(base_text)
    new_signature = analyze_signature(new_text)
    
    deviation = compare_signatures(base_signature, new_signature)
    alert_result = check_for_impersonation(base_signature, new_signature)
    
    print("Test LexGuard Module:")
    print("Base Signature:", base_signature)
    print("New Signature:", new_signature)
    print("Signature Deviation:", deviation)
    print("Alert Result:", alert_result)

test_lexguard()
