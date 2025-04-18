from fastapi import FastAPI


application = FastAPI()

@application.get("/")
def read_root():
    return {"message": "Hello, World!"}

@application.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@application.get("/home")
def read_home():
    return {"home": "Address de ma maison."}