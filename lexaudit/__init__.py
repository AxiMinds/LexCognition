# lexaudit/__init__.py

from datetime import datetime
import hashlib

def generate_audit_report(text: str, metadata: dict, previous_version: dict = None) -> dict:
    """
    Generate a comprehensive audit report for the given text.

    Args:
    text (str): The input text to analyze.
    metadata (dict): Additional information about the text.
    previous_version (dict): The previous version of the text for change tracking.

    Returns:
    dict: A dictionary containing the audit report.
    """
    word_count = len(text.split())
    char_count = len(text)
    average_word_length = char_count / word_count if word_count > 0 else 0
    
    # Generate a hash of the text for version control
    text_hash = hashlib.md5(text.encode()).hexdigest()

    report = {
        "timestamp": datetime.now().isoformat(),
        "text_stats": {
            "word_count": word_count,
            "character_count": char_count,
            "average_word_length": round(average_word_length, 2)
        },
        "metadata": metadata,
        "version_control": {
            "hash": text_hash
        },
        "audit_summary": f"Audit completed for text with {word_count} words and {char_count} characters."
    }

    # If we have a previous version, track changes
    if previous_version:
        changes = {
            "word_count_change": word_count - previous_version["text_stats"]["word_count"],
            "char_count_change": char_count - previous_version["text_stats"]["character_count"],
            "avg_word_length_change": round(average_word_length - previous_version["text_stats"]["average_word_length"], 2)
        }
        report["changes"] = changes
        report["audit_summary"] += f" Changes detected from previous version."

    return report