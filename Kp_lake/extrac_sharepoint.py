import requests

# URL de l'API SharePoint pour obtenir les informations sur les fichiers
api_url = "https://connectin.ingroupe.com/team/SfFrontOffice/_api/web/getfolderbyserverrelativeurl('/team/SfFrontOffice/Documents%20partages/02%20-%20Squad%20Identity%20Station')/files"

# Remplacez 'votre_nom_utilisateur' et 'votre_mot_de_passe' par vos identifiants SharePoint
username = 'tburdinat'
password = '?MWRL1R8if'

# Envoyer une requête GET à l'API SharePoint pour obtenir les informations sur les fichiers
response = requests.get(api_url, auth=(username, password))

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()
    # Parcourir les fichiers et afficher leurs URLs
    for file in data['value']:
        print("Nom du fichier:", file['Name'])
        print("URL du fichier:", file['ServerRelativeUrl'])
else:
    print("Erreur lors de la récupération des fichiers:", response.status_code)
