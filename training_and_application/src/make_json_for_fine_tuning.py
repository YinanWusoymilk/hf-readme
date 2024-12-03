import pandas as pd
import json

# Load the Excel file
file_path = 'final_categorized_data.xlsx'
df = pd.read_excel(file_path)

# Define sections
sections = [
    "Introduction/Model Description",
    "Usage/How to Use/Where to Use",
    "Model Limitations",
    "Evaluation/Performance/Results",
    "Training Info",
    "Citation/References",
    "License",
    "Contributions and Acknowledgement"
]

# List of invalid tokens to replace
invalid_tokens = [
    "<|endoftext|>",  # Reserved token in OpenAI models
    "<|startoftext|>",  # Reserved token in OpenAI models
    "<|assistant|>",  # Potentially reserved token for role
    "<|user|>",  # Potentially reserved token for role
    "<|system|>",  # Potentially reserved token for role
    "<|newline|>",  # Custom tokens might be misinterpreted
    "<|padding|>",  # Reserved for internal use
    "<|mask|>",  # Reserved for special tasks
    "\u0000",  # Null character
    "\u2028",  # Line separator (can cause issues in JSON)
    "\u2029",  # Paragraph separator (can cause issues in JSON)
    "\r",  # Carriage return
    "\t",  # Tab character (for cleaner formatting)
    "<|im_start|>",
    "<|im_end|>"
]

# Function to clean invalid tokens from text
def clean_invalid_tokens(text):
    if not isinstance(text, str):
        return text
    for token in invalid_tokens:
        text = text.replace(token, "")
    return text.strip()

# Create JSONL data for chat format
jsonl_data = []

for _, row in df.iterrows():
    # Clean the README text
    readme_text = clean_invalid_tokens(str(row['Full Readme Text']))

    # Construct the system message
    system_message = {
        "role": "system",
        "content": (
            "You are an intelligent system that analyzes README files from Hugging Face models. "
            "Your task is to extract and classify 8 key components from the README content provided below. "
            "Identify whether each component is present or absent and provide the content of each present component."
        )
    }

    # Construct the user message
    user_message = {
        "role": "user",
        "content": f"README Content:\n---\n{readme_text}\n---"
    }

    # Construct the assistant message
    completion_parts = []
    present_sections = []
    absent_sections = []
    for section in sections:
        if pd.notnull(row[section]):
            content = clean_invalid_tokens(str(row[section]))
            completion_parts.append(
                f"Status of {section}: PRESENT\n\n  Content related to {section} identified in the README: {content}"
            )
            present_sections.append(section)
        else:
            completion_parts.append(f"Status of {section}: ABSENT")
            absent_sections.append(section)
    completion_parts = (
        "\n".join(completion_parts) +
        "\n\n\nList of Present Sections:" + ", ".join(present_sections) +
        "\n\n\nList of Absent Sections:" + ", ".join(absent_sections)
    )
    assistant_message = {
        "role": "assistant",
        "content": completion_parts
    }

    # Add to JSONL data
    jsonl_data.append({
        "messages": [system_message, user_message, assistant_message]
    })

# Save as JSONL
output_path = 'readme_sections_with_chat_format.jsonl'
with open(output_path, 'w', encoding='utf-8') as f:
    for entry in jsonl_data:
        json.dump(entry, f, ensure_ascii=False)  # Ensure proper encoding
        f.write('\n')

print(f"Chat-formatted dataset saved to {output_path}")
