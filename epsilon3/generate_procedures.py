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

        safety_notice = ""
        
        for subcontent in step['content']:
            if subcontent['type'] == 'alert' and subcontent['subtype'] == 'caution':
                safety_notice = subcontent['text'] + "\lcwarning"
            elif subcontent['type'] == 'alert' and subcontent['subtype'] == 'warning':
                safety_notice = subcontent['text'] + "\lccritical"
            elif subcontent['type'] == 'text':
                text = subcontent['text']
                text = text.replace("\n", ".").replace("-", "")
                step_name = step_name + text + "."

        operator_notice = ""
        print(step["signoffs"])
        for signoff in step["signoffs"]:
            role = signoff["operators"]
            if len(role) == 0:
                operator_notice += "CE, "
            elif len(role) == 1:
                operator_notice += role[0] + ", "
            elif len(role) > 1:
                for i in range(len(role)):
                    operator_notice += role[i] + ", "
        operator_notice = operator_notice[:-2]
        print(operator_notice)
        print("\n")
        
        latex_row = f"    {section_counter}.{subsection_counter} & {safety_notice} & Gloves & {operator_notice} & \\checkbox {step_name}\\\\\\hline"
        latex_output.append(latex_row)

        operator_notice = ""

        subsection_counter += 1
    
    subsection_counter = 1

    # End the launch checklist command for the current section
    latex_output.append("}")

    latex_output.append(f"{{{section_name}}}{{{label_name}}}\n\n")

    # Increment section number after processing each section
    section_counter += 1
    # Reset subsection counter for the next section

    # Join all the LaTeX lines together into one string
    latex_code = "".join(latex_output)
    print("Completed section:", section['name'])
    print("")

# Write the LaTeX code to a text file named after the section name
with open(write_path, 'w') as output_file:
    output_file.write(latex_code)

print(f"LaTeX code has been written to {write_path}")