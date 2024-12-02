import pandas as pd
from collections import defaultdict

def process_excel(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    
    processed_data = [] 
    label_count = defaultdict(int)
    
    for index, row in df.iterrows():
        content_dict = {}
        for i in range(0, len(row), 2):
            content = row[i] if pd.notna(row[i]) else ""
            label = row[i+1] if (i+1 < len(row) and pd.notna(row[i+1])) else ""

            if label in ["For later use", "Ignore"]:
                continue

            if label == "Introduction":
                label = "Model Description"
            
            if label == "Dataset":
                label = "training info"

            if label in ["Intended Usage", "Intended Use", "Ethical Usage"]:
                label = "Usage(How to Use)"
            
            if label == "Bias":
                label = "Model Limitations"

            if label != '' and label not in content_dict:
                label_count[label] += 1
            
            if label in content_dict:
                content_dict[label] += str(content)
            else:
                content_dict[label] = str(content)
        
        processed_data.append(content_dict)
    
    result_df = pd.DataFrame(processed_data)
    result_df.to_excel("processed_data.xlsx", index=False)
    
    label_count_df = pd.DataFrame(list(label_count.items()), columns=['Label', 'Count'])
    label_count_df.to_excel("label_counts.xlsx", index=False)

process_excel("markdown_headers.xlsx", "Sheet2")
