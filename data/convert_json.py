import json
import re
from training_data import questions, problems, statements

def convert_to_jsonl(text, category):
    """
    Convert a text string of questions into JSONL format with categories
    
    Args:
        text (str): The text containing questions
        category (str): The category to assign to these questions
        
    Returns:
        list: List of dictionaries ready for JSONL conversion
    """
    # Split the text into lines and clean them
    lines = text.strip().split('\n')
    
    # Remove empty lines and clean up each line
    questions = []
    for line in lines:
        # Remove whitespace
        cleaned = line.strip()
        
        # Remove numbering only if line starts with numbers followed by period
        if re.match(r'^\d+\.', cleaned):
            cleaned = re.sub(r'^\d+\.\s*', '', cleaned)
            
        if cleaned:  # Only add non-empty lines
            questions.append(cleaned)
    
    # Create JSONL format
    jsonl_data = []
    for question in questions:
        entry = {
            "category": category,
            "conversation": question
        }
        jsonl_data.append(entry)
    
    return jsonl_data

def main():
    # Convert all categories
    all_data = []
    
    # Convert therapy questions
    all_data.extend(convert_to_jsonl(questions, "questions"))
    
    # Convert career questions
    all_data.extend(convert_to_jsonl(problems, "problems"))
    
    # Convert relationship questions
    all_data.extend(convert_to_jsonl(statements, "statements"))
    
    # Write to file using ensure_ascii=False to preserve Unicode characters
    with open('training_data.jsonl', 'w', encoding='utf-8') as f:
        for entry in all_data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    # Preview first few entries from each category
    print("Preview of converted questions:")
    for entry in all_data[:3]:
        print(json.dumps(entry, ensure_ascii=False))

if __name__ == "__main__":
    main()