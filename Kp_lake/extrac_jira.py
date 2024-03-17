
a="MTM5NDYwMDc4MDM0OmGWoQKOXRk10/kvIEP2HbxU7BCJ"
import json
import subprocess
#data d'identifcation
JIRA_URL = "https://jira.in-idt-ivv.local"
API_VERSION = "2"
PROJECT_KEY = "BQR"
TOKEN = a

# URL de l'API
API_URL = f"{JIRA_URL}/rest/api/{API_VERSION}/search"

#la requête JQL pour rechercher les tickets du projet spécifié
JQL_QUERY = f"project={PROJECT_KEY}"

#URL finale
URL_WITH_QUERY = f"{API_URL}?jql={JQL_QUERY}&maxResults=500"  #nombre maximum de resultats

#commande cURL 
curl_command = f'curl -H "Authorization: Bearer {TOKEN}" "{URL_WITH_QUERY}"'

output = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

if output.returncode == 0:
    response_data = json.loads(output.stdout)
    
    for issue in response_data['issues']:
        issue_id = issue['id']
        issue_key = issue['key']
        issue_status = issue['fields']['status']['name']
        created_date = issue['fields']['created']
        print(f"Issue ID: {issue_id}, Key: {issue_key}, Status: {issue_status}, Created Date: {created_date}")
else:
    print("La commande cURL a échoué.")