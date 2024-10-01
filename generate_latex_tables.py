import pandas as pd
import os

# Test update from github
# Test again!

def generate_latex_table_fmea(data, table_name, table_ref):
    latex_table = f"\\fmeaCDR{{"
    
    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        risk = str(row['Failure Mode'])
        description = str(row['Cause'])
        effect = str(row['Effect'])
        pre_rac = str(row['Pre-RAC'])
        mitigation = str(row['Mitigation'])
        verification = str(row['Verification'])
        post_rac = str(row['Post-RAC'])
        
        latex_row = f"{risk}&{description}&{effect}&\{pre_rac}&{mitigation}&{verification}&\{post_rac}\\\\\hline "
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row

    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def generate_latex_table_nasa_requirements_proposal(data, table_name, table_ref):
    latex_table = f"\\requirementsPROPOSAL{{"

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        item = str(row['Item'])
        description = str(row['Description'])
        justification = str(row['Specification'])
        
        latex_row = f"{item}&{description}&{justification}\\\\\hline "
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def generate_latex_table_risks(data, table_name, table_ref):
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
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def generate_latex_table_team_requirements(data, table_name, table_ref):
    latex_table = f"\\requirementsCDR{{"

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        item = str(row['Item'])
        description = str(row['Description'])
        verification_method = str(row['Verification Method'])
        verification_status = str(row['Verification Status'])
        section = str(row['Section'])
        
        latex_row = f"{item}&{description}&{verification_method}&{verification_status}&{section}\\\\\hline "
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def generate_latex_table_nasa_requirements(data, table_name, table_ref):
    latex_table = f"\\requirementsCDR{{"

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        item = str(row['Item'])
        description = str(row['Description'])
        verification_method = str(row['Verification Method'])
        verification_status = str(row['Verification Status'])
        section = str(row['Section'])
        
        latex_row = f"{item}&{description}&{verification_method}&{verification_status}&{section}\\\\\hline "
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def generate_latex_table_overallBudget(data, table_name, table_ref):
    latex_table = f"\\overallBudget{{"

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        project = str(row['Project'])
        total = str(row['Total'])
        
        latex_row = f"{project}&{total}\\\\\hline "
        # latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#')
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def generate_latex_table_itemizedBudget(data, table_name, table_ref):
    latex_table = f"\\itemizedBudget{{"

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        item = str(row['Item'])
        description = str(row['Description'])
        vendor = str(row['Vendor'])
        unit_cost = str(row['Unit Cost'])
        count = str(row['Count'])
        total = str(row['Total'])
        
        latex_row = f"{item}&{description}&{vendor}&{unit_cost}&{count}&{total}\\\\\hline "
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def generate_latex_table_challenges_solutions(data, table_name, table_ref):
    latex_table = f"\\challengesSolutions{{"

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        challenge = str(row['Challenge'])
        solution = str(row['Solution'])
        
        latex_row = f"{challenge}&{solution}\\\\\hline "
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table
    
def generate_latex_table_changes(data, table_name, table_ref):
    latex_table = f"\\changes{{"

    # Iterate through each row in the DataFrame and convert to LaTeX format
    for index, row in data.iterrows():

        criteria = str(row['Criteria'])
        previous = str(row['Previous Report'])
        current = str(row['Current'])

        
        latex_row = f"{criteria}&{previous}&{current}\\\\\hline "
        latex_row = latex_row.replace('\n', '').replace('%', '\\%').replace('$', '\\$').replace('#', '\\#').replace('^', '\\^')
        latex_table += latex_row
    
    latex_table += f"}}{{{table_name}}}{{{table_ref}}}\n"
    return latex_table

def parse_excel_file(file_path_header, file_path):
    # Read the Excel file
    xls = pd.ExcelFile(file_path_header + file_path + ".xlsx")

    all_tables = ""

    # Iterate through each sheet in the workbook
    for sheet_name in xls.sheet_names:

        if sheet_name != "IGNORE":
            
            df = pd.read_excel(xls, sheet_name=sheet_name)

            table_name = df["metadata"][0]
            table_ref = df["metadata"][1]

            if "budget" in file_path:
                if sheet_name == "Overall":
                    latex_table = generate_latex_table_overallBudget(df, table_name, table_ref)
                else:
                    latex_table = generate_latex_table_itemizedBudget(df, table_name, table_ref)
            elif "fmea" in file_path:
                    latex_table = generate_latex_table_fmea(df, table_name, table_ref)
            elif "nasa_requirements_proposal" in file_path:
                    latex_table = generate_latex_table_nasa_requirements_proposal(df, table_name, table_ref)
            elif "nasa_requirements" in file_path:
                    latex_table = generate_latex_table_nasa_requirements(df, table_name, table_ref)
            elif "risks" in file_path:
                    latex_table = generate_latex_table_risks(df, table_name, table_ref)
            elif "team_requirements" in file_path:
                    latex_table = generate_latex_table_team_requirements(df, table_name, table_ref)
            elif "challenges_solutions" in file_path:
                    latex_table = generate_latex_table_challenges_solutions(df, table_name, table_ref)
            elif "changes" in file_path:
                    latex_table = generate_latex_table_changes(df, table_name, table_ref)
            else:
                print("Error: File not recognized")
                return
     
            # Generate the LaTeX table string
            print("Generating LaTeX table for:", table_name)
        
            # print(latex_table)
            all_tables += latex_table + "\n"

    all_tables = all_tables.replace('nan', '') # empty values

    with open(file_path_header + file_path + ".txt", 'w') as file:
        file.write(all_tables)
    

file_path_header = '/Users/andrewwehmeyer/Downloads/'
files = ['budget', 'fmea', 'nasa_requirements_proposal', 'nasa_requirements', 'risks', 'team_requirements', 'challenges_solutions', 'changes']

for file in files:
    file_path = os.path.join(file_path_header, file + '.xlsx')  # Assuming the files are .xlsx
    if os.path.exists(file_path):
        parse_excel_file(file_path_header, file)
    else:
        # print(f"File {file} not found. Skipping...")
        pass

#  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
# | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
# | |   _____      | || |      __      | || |  _________   | || |  _________   | || |  ____  ____  | |
# | |  |_   _|     | || |     /  \     | || | |  _   _  |  | || | |_   ___  |  | || | |_  _||_  _| | |
# | |    | |       | || |    / /\ \    | || | |_/ | | \_|  | || |   | |_  \_|  | || |   \ \  / /   | |
# | |    | |   _   | || |   / ____ \   | || |     | |      | || |   |  _|  _   | || |    > `' <    | |
# | |   _| |__/ |  | || | _/ /    \ \_ | || |    _| |_     | || |  _| |___/ |  | || |  _/ /'`\ \_  | |
# | |  |________|  | || ||____|  |____|| || |   |_____|    | || | |_________|  | || | |____||____| | |
# | |              | || |              | || |              | || |              | || |              | |
# | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

# change the file_path_header to be appropriate for your computer
# download the files you wish to generate -- do not modify the file names
# run