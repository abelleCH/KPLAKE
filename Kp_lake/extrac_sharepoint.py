import requests

# URL de l'API SharePoint pour obtenir les informations sur le dossier "Documents partages"
api_url = "https://connectin.ingroupe.com/team/SfFrontOffice/_api/web/getfolderbyserverrelativeurl('/team/SfFrontOffice/Documents partages')"

# Remplacez 'votre_nom_utilisateur' et 'votre_mot_de_passe' par vos identifiants SharePoint
username = 'tburdinat'
password = '?MWRL1R8if'

# Envoyer une requête GET à l'API SharePoint pour obtenir les informations sur le dossier "Documents partages"
response = requests.get(api_url, auth=(username, password))

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Parcourir les dossiers pour trouver le dossier "02 - Squad Identity Station"
    for folder in data['Folders']:
        if folder['Name'] == '02 - Squad Identity Station':
            # Récupérer l'URL du dossier "02 - Squad Identity Station"
            folder_url = folder['ServerRelativeUrl']

            # Récupérer les fichiers du dossier "02 - Squad Identity Station"
            files_url = f"https://connectin.ingroupe.com/team/SfFrontOffice/_api/web/getfolderbyserverrelativeurl('{folder_url}')/files"
            files_response = requests.get(files_url, auth=(username, password))

            # Vérifier si la requête a réussi
            if files_response.status_code == 200:
                files_data = files_response.json()

                # Parcourir les fichiers pour trouver le fichier "02 - Squad Identity Station"
                for file in files_data['value']:
                    if file['Name'] == '02 - Squad Identity Station':
                        print("Nom du fichier:", file['Name'])
                        print("URL du fichier:", file['ServerRelativeUrl'])
                        print("Taille du fichier:", file['Length'])
            else:
                print("Erreur lors de la récupération des fichiers du dossier:", files_response.status_code)
else:
    print("Erreur lors de la récupération des informations sur le dossier:", response.status_code)
