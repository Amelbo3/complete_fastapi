from fastapi import FastAPI


application = FastAPI()

@application.get("/")
def read_root():
    return {"message": "Hello, World!"}

@application.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@application.get("/email/{email}")
def read_email(email):
    if email == 'amelbo3@gmail.com':
    
        nom = "Amadou"
        prenom = "Elhadj"
        dob = "04/27/1974"
        city = "Charlotte"
        phone = "980-333-5085"

        mes_donnees = {"nom": nom, "prenom": prenom, "dob": dob, "city": city, "phone": phone}
    else:

        mes_donnees = {"nom": "", "prenom": "", "dob": "", "city": "", "phone": ""}
    

    return mes_donnees