import pandas as pd
import os

# Load the uploaded Excel file
file_path = 'Paul processed_data.xlsx'
data = pd.read_excel(file_path)

# Directory where README files are located
directory_path = '../readme_files'  # Update this to your actual directory path

# Function to search for README file and get its content
def find_readme_content(file_name, directory):
    file_name = file_name+'.md'
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "File not found"

# Process each file in the Excel sheet
data['Readmetext'] = data['Modelname'].apply(lambda x: find_readme_content(x, directory_path))

# Save the updated Excel file
output_path = 'Processed_Paul_processed_data.xlsx'
data.to_excel(output_path, index=False)

print(f"Processed file saved to: {output_path}")
