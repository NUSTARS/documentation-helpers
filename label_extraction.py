# import os
# import re
# import pandas as pd

# def extract_labels_from_tex(file_path):
#     """
#     Extract all \label{} tags from a .tex file.

#     Args:
#         file_path (str): Path to the .tex file.

#     Returns:
#         list: A list of all labels found in the file.
#     """
#     labels = []
#     label_pattern = re.compile(r'\\label\{(.*?)\}')
    
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             matches = label_pattern.findall(line)
#             labels.extend(matches)
    
#     return labels

# def find_all_tex_files(root_folder):
#     """
#     Traverse the directory tree to find all main.tex files.

#     Args:
#         root_folder (str): Path to the root directory.

#     Returns:
#         list: A list of paths to main.tex files.
#     """
#     tex_files = []
#     for dirpath, _, filenames in os.walk(root_folder):
#         for filename in filenames:
#             if filename == "main.tex":
#                 tex_files.append(os.path.join(dirpath, filename))
#     return tex_files

# def main(root_folder, output_file):
#     """
#     Extract all \label{} tags from all main.tex files in the directory and save to spreadsheet.

#     Args:
#         root_folder (str): Path to the root folder containing the SRC folder.
#         output_file (str): Path to save the output spreadsheet.
#     """
#     all_labels = []

#     # Find all main.tex files
#     tex_files = find_all_tex_files(root_folder)
#     print(f"Found {len(tex_files)} main.tex files.")

#     # Extract labels from each file
#     for tex_file in tex_files:
#         labels = extract_labels_from_tex(tex_file)
#         all_labels.extend(labels)
#         print(f"Extracted {len(labels)} labels from {tex_file}")

#     # Save to Excel file
#     df = pd.DataFrame(all_labels, columns=["Labels"])
#     df.to_excel(output_file, index=False)
#     print(f"Labels saved to {output_file}")

# # Run the script
# file_path_header = '/Users/andrewwehmeyer/Downloads/NUSTARS-SRC'
# output_file = 'extracted_labels.xlsx'
# main(file_path_header, output_file)

import os
import re
import pandas as pd

def extract_labels_from_tex(file_path, pattern):
    """
    Extract all matching patterns from a .tex file.

    Args:
        file_path (str): Path to the .tex file.
        pattern (str): Regex pattern to match specific tags.

    Returns:
        list: A list of all matches found in the file.
    """
    matches = []
    label_pattern = re.compile(pattern)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches.extend(label_pattern.findall(line))
    
    return matches

def find_all_tex_files(root_folder, extension=".tex", folder_filter=None):
    """
    Traverse the directory tree to find all files with the given extension,
    optionally filtering by folder name.

    Args:
        root_folder (str): Path to the root directory.
        extension (str): File extension to look for (default is ".tex").
        folder_filter (str, optional): Folder name to filter by (e.g., "spreadsheets").

    Returns:
        list: A list of paths to files with the specified extension in folders matching folder_filter.
    """
    tex_files = []
    for dirpath, _, filenames in os.walk(root_folder):
        if folder_filter and folder_filter not in os.path.basename(dirpath):
            continue
        for filename in filenames:
            if filename.endswith(extension):
                tex_files.append(os.path.join(dirpath, filename))
    return tex_files


def main(root_folder, output_file):
    """
    Extract all \label{} tags from main.tex files and {tab: ...} from spreadsheet tex files.

    Args:
        root_folder (str): Path to the root folder containing SRC and spreadsheets.
        output_file (str): Path to save the output spreadsheet.
    """
    all_labels = []

    # Extract \label{} tags from all main.tex files in SRC directory
    src_files = find_all_tex_files(os.path.join(root_folder, "SRC"), "main.tex")
    print(f"Found {len(src_files)} main.tex files in SRC.")

    for tex_file in src_files:
        labels = extract_labels_from_tex(tex_file, r'\\label\{(.*?)\}')
        all_labels.extend([{"Label_Type": "Label", "Text": label} for label in labels])
        print(f"Extracted {len(labels)} labels from {tex_file}")

    # Extract {tab: ...} from all .tex files in any "spreadsheets" folder
    spreadsheet_files = find_all_tex_files(root_folder, ".tex", folder_filter="spreadsheets")
    print(f"Found {len(spreadsheet_files)} .tex files in 'spreadsheets' folders.")

    for tex_file in spreadsheet_files:
        table_labels = extract_labels_from_tex(tex_file, r'\{tab:(.*?)\}')
        all_labels.extend([{"Label_Type": "Table", "Text": "tab:" + label} for label in table_labels])
        print(f"Extracted {len(table_labels)} table labels from {tex_file}")

    # Save to Excel file
    df = pd.DataFrame(all_labels)
    df.to_csv(output_file, index=False, columns=["Text"])
    print(f"Labels and table identifiers saved to {output_file}")

# Run the script
file_path_header = '/Users/andrewwehmeyer/Downloads/NUSTARS-SRC/'
output_file = 'labels.csv'
main(file_path_header, output_file)
