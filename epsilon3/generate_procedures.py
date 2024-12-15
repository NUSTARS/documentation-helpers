import json
from pathlib import Path

project_root = Path(__file__).parent  # Gets the current directory where the script is located
read_path = project_root / "full_scale.json"
write_path = project_root / "full_scale_procedures.tex"

# Read the JSON data from a file
with open(read_path, 'r') as file:
    json_data = json.load(file)

# Initialize section and subsection counters
section_counter = 1
subsection_counter = 1

# Start building the LaTeX input for the launch checklist
latex_output = []

for section in json_data['sections']:
    print("Processing section:", section['name'])
    # Get the section name to be used as the table caption
    section_name =  section['name']
    
    # Use a generic label for referencing later
    label_name = f"tab:safety:{section_name.replace(' ', '_').lower()}"

    # Start the launch checklist command without the section header on the first line
    latex_output.append(f"\\launchchecklist{{")

    for step in section['steps']:
        step_name = step['name']
        
        # for alert in step['content']:
        #     if alert['type'] == 'alert' and alert['subtype'] in ['warning', 'caution']:
        #         # Construct the LaTeX row for each step, including step number, step name, alert type, PPE, and personnel
        #         latex_row = f"    {section_counter}.{subsection_counter} & \\lccritical {alert['subtype'].capitalize()} & Gloves & CE & \\checkbox {step_name}\\\\\\hline"
        #         latex_output.append(latex_row)

        #         # Increment the subsection counter for each new step
        
        latex_row = f"    {section_counter}.{subsection_counter} & \\lccritical & Gloves & CE & \\checkbox {step_name}\\\\\\hline"
        latex_output.append(latex_row)

        subsection_counter += 1
    
    subsection_counter = 1

    # End the launch checklist command for the current section
    latex_output.append("}")

    latex_output.append(f"{{{section_name}}}{{{label_name}}}\n\n")

    # Increment section number after processing each section
    section_counter += 1
    # Reset subsection counter for the next section

    print(latex_output)

    # Join all the LaTeX lines together into one string
    latex_code = "".join(latex_output)
    print("Completed section:", section['name'])
    print("\n")

# Write the LaTeX code to a text file named after the section name
with open(write_path, 'w') as output_file:
    output_file.write(latex_code)

print(f"LaTeX code has been written to {write_path}")