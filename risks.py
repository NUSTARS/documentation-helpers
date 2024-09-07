import pandas as pd

def generate_latex_table(data, table_name, table_ref):
    latex_table = f"\\risksCDR{{"
    

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        risk = str(row['Hazard/Risk'])
        description = str(row['Cause'])
        effect = str(row['Effect'])
        pre_rac = str(row['Pre-RAC'])
        mitigation = str(row['Mitigation'])
        verification = str(row['Verification'])
        post_rac = str(row['Post-RAC'])
        
        latex_row = f"{risk}&{description}&{effect}&\{pre_rac}&{mitigation}&{verification}&\{post_rac}\\\\\hline "
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

            # print(df.head())
    
            table_name = df["metadata"][0]
            table_ref = df["metadata"][1]
                    
            # Generate the LaTeX table string
            latex_table = generate_latex_table(df, table_name, table_ref)

            print("Generating LaTeX table for:", table_name)
            
            all_tables += latex_table + "\n"

    all_tables = all_tables.replace('nan', '') # empty values

    with open('/Users/andrewwehmeyer/Downloads/risks_formatted.txt', 'w') as file:
        file.write(all_tables)

# Path to your Excel file
file_path = '/Users/andrewwehmeyer/Downloads/risks.xlsx'

# Parse the Excel file and generate LaTeX tables
parse_excel_file(file_path)
