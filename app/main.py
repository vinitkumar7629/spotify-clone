from fastapi import FastAPI

app= FastAPI(title="spotify clone")

@app.get("/")
def home():
    return{"message":"spotify clone is running!"}