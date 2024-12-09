import requests
import os
import json

# Check and print the API key for debugging
api_key = os.environ.get('EPSILON3_API_KEY')
if not api_key:
    raise ValueError("API key is missing. Set the EPSILON3_API_KEY environment variable.")
print(f"Using API Key: {api_key[:5]}... (hidden for security)")

# API details
# procedure_id = 'LF2oRIWnNAVLb0OUztiom4' # subscale
# procedure_id = 'zXpyGHRlJSGR2H70eNVqlB' # fullscale
procedure_id = 'OSkODboL2gPoBFCY7AOfTc' # teaching chat how to do this

base_url = 'https://api.epsilon3.io/v1' 
endpoint = f"{base_url}/procedures/{procedure_id}"

# Headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

print(endpoint)

response = requests.get(
    url=endpoint,
    auth=(api_key, ''),
    headers=headers
)

print(response.status_code)
json_data = response.json()

# output_file = "subscale_procedure.json"
output_file = "chat_teaching.json"

with open(output_file, "w") as file:
    json.dump(json_data, file, indent=4)  # Pretty print with 4-space indentation
