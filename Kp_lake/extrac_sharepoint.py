import requests

# URL de l'API SharePoint pour récupérer les éléments d'une liste ou d'une bibliothèque
api_url = "https://connectin.ingroupe.com/_api/web"

# Remplacez 'votre_nom_utilisateur' et 'votre_mot_de_passe' par vos identifiants SharePoint
username = 'tburdinat'
password = '?MWRL1R8if'

# Envoyer une requête GET à l'API SharePoint pour récupérer les dossiers
response = requests.get(api_url, auth=(username, password),verify=False)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()
    # Parcourir les dossiers et les afficher
    for folder in data['value']:
        print("Dossier:", folder['Name'])
    
    # Récupérer les fichiers
    files_url = "https://connectin.ingroupe.com/team/SfFrontOffice/_api/web/getfolderbyserverrelativeurl('/team/SfFrontOffice/Documents partages/02 - Squad Identity Station/15 - Gabon LCU (GROAD)/Livraisons')/files"
    files_response = requests.get(files_url, auth=(username, password))
    
    if files_response.status_code == 200:
        files_data = files_response.json()
        # Parcourir les fichiers et les afficher
        for file in files_data['value']:
            print("Fichier:", file['Name'])
    else:
        print("Erreur lors de la récupération des fichiers:", files_response.status_code)
else:
    print("Erreur lors de la récupération des dossiers:", response.status_code)
