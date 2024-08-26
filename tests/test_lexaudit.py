from lexaudit.version_control import track_changes, save_version_control
from lexaudit.change_analysis import analyze_changes, load_version_control
from lexaudit.audit_report_generation import generate_audit_report

def test_lexaudit():
    original_text = "This is the original text. It will be modified."
    revised_text = "This is the modified text. It has been changed."
    
    # Track changes and save version control
    diff = track_changes(original_text, revised_text)
    save_version_control(diff, filename="test_version_control.json")
    
    # Load version control and analyze changes
    diff_loaded = load_version_control(filename="test_version_control.json")
    analysis = analyze_changes(diff_loaded)
    
    # Generate audit report
    report = generate_audit_report(filename="test_version_control.json")
    
    print("Test LexAudit Module:")
    print("Change Analysis:", analysis)
    print("Audit Report:\n", report)

test_lexaudit()
