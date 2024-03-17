import requests

API_URL = 'https://sonarqube.in-idt-ivv.local/api'
API_TOKEN = 'squ_7f3092c8ebeb4de4eaa3b14741cfb365f1eea7f2'

headers={
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.get(f"{API_URL}/user_tokens/search", auth=(API_TOKEN, ''), headers=headers, verify=False)

print(response.json())
