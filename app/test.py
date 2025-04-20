import requests


email = "amelbo3@gmail.com"
add_url = "http://localhost:8000/email/"

resultat = requests.get(add_url + email)
if resultat.status_code == 200:
    data = resultat.json()
    print(data)
