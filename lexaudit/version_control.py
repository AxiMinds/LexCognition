import difflib
import json

def track_changes(original_text, revised_text):
    diff = list(difflib.ndiff(original_text.splitlines(), revised_text.splitlines()))
    return diff

def save_version_control(diff, filename="version_control.json"):
    with open(filename, 'w') as file:
        json.dump(diff, file, indent=4)

if __name__ == "__main__":
    original_text = "This is the original text. It will be modified."
    revised_text = "This is the modified text. It has been changed."

    diff = track_changes(original_text, revised_text)
    save_version_control(diff)

    print("Version Control Data Saved.")
