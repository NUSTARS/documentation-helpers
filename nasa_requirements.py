import pandas as pd

def generate_latex_table(data, table_name, table_ref):
    latex_table = f"\\requirementsCDR{{"

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        item = str(row['Item'])
        description = str(row['Description'])
        verification_method = str(row['Verification Method'])
        verification_status = str(row['Verification Status'])
        section = str(row['Section'])
        
        latex_row = f"{item}&{description}&{verification_method}&{verification_status}&{section}\\\\\hline"
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def parse_excel_file(file_path):
    # Read the Excel file
    xls = pd.ExcelFile(file_path)

    all_tables = ""

    # Iterate through each sheet in the workbook
    for sheet_name in xls.sheet_names:

        if sheet_name != "IGNORE":
            
            df = pd.read_excel(xls, sheet_name=sheet_name)

            table_name = df["metadata"][0]
            table_ref = df["metadata"][1]
                    
            # Generate the LaTeX table string
            latex_table = generate_latex_table(df, table_name, table_ref)

            print("Generating LaTeX table for:", table_name)
        
        # print(latex_table)
        all_tables += latex_table + "\n"

    all_tables = all_tables.replace('nan', '') # empty values

    with open('/Users/andrewwehmeyer/Downloads/nasa_requirements_formatted.txt', 'w') as file:
        file.write(all_tables)

# Path to your Excel file
file_path = '/Users/andrewwehmeyer/Downloads/nasa_requirements.xlsx'

# Parse the Excel file and generate LaTeX tables
parse_excel_file(file_path)
