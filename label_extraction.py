import os
import re
import pandas as pd

def extract_labels_from_tex(file_path):
    """
    Extract all \label{} tags from a .tex file.

    Args:
        file_path (str): Path to the .tex file.

    Returns:
        list: A list of all labels found in the file.
    """
    labels = []
    label_pattern = re.compile(r'\\label\{(.*?)\}')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = label_pattern.findall(line)
            labels.extend(matches)
    
    return labels

def find_all_tex_files(root_folder):
    """
    Traverse the directory tree to find all main.tex files.

    Args:
        root_folder (str): Path to the root directory.

    Returns:
        list: A list of paths to main.tex files.
    """
    tex_files = []
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename == "main.tex":
                tex_files.append(os.path.join(dirpath, filename))
    return tex_files

def main(root_folder, output_file):
    """
    Extract all \label{} tags from all main.tex files in the directory and save to spreadsheet.

    Args:
        root_folder (str): Path to the root folder containing the SRC folder.
        output_file (str): Path to save the output spreadsheet.
    """
    all_labels = []

    # Find all main.tex files
    tex_files = find_all_tex_files(root_folder)
    print(f"Found {len(tex_files)} main.tex files.")

    # Extract labels from each file
    for tex_file in tex_files:
        labels = extract_labels_from_tex(tex_file)
        all_labels.extend(labels)
        print(f"Extracted {len(labels)} labels from {tex_file}")

    # Save to Excel file
    df = pd.DataFrame(all_labels, columns=["Labels"])
    df.to_csv(output_file, index=False)
    print(f"Labels saved to {output_file}")

# Run the script
root_folder = '/Users/andrewwehmeyer/Downloads/NUSTARS-SRC/'  # Replace with the path to your SRC folder
output_file = 'extracted_labels.csv'
main(root_folder, output_file)
