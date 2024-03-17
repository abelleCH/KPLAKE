import requests

url = "https://connectin.ingroupe.com/team/SfFrontOffice/SitePages/Accueil.aspx"
response = requests.get(url)

if response.status_code == 200:
    print("Requête réussie !")
else:
    print("Erreur lors de la requête :", response.status_code)

# # Remplacez ces valeurs par les vôtres
# site_url = "https://connectin.ingroupe.com/team/SfFrontOffice/SitePages/Accueil.aspx"
# file_relative_url = "RootFolder=%2Fteam%2FSfFrontOffice%2FDocuments%20partages%2F02%20-%20Squad%20Identity%20Station&FolderCTID=0x012000171359A7C53D494DB5D00E85CEC98595&View=%7BC4D67FB1-BE2D-45C5-9904-02C48F283546%7D"  # Spécifiez le chemin relatif du fichier à partir du site SharePoint

# # URL de l'API REST pour obtenir les informations sur le fichier spécifié
# api_url = f"{site_url}/_api/web/getfilebyserverrelativeurl('{file_relative_url}')"

# # Headers requis pour spécifier le type de contenu et l'authentification
# headers = {
#     "Accept": "application/json;odata=verbose",
#     "Content-Type": "application/json;odata=verbose"
# }

# # Envoyer une requête GET à l'API SharePoint pour obtenir les informations sur le fichier
# response = requests.get(api_url, headers=headers)

# # Vérifier si la requête a réussi (code de statut HTTP 200)
# if response.status_code == 200:
#     data = response.json()
#     # Extraire et afficher le nom du fichier
#     file_name = data['d']['Name']
#     print("Nom du fichier :", file_name)
# else:
#     print("Erreur lors de la requête :", response.status_code)