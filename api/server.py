from fastapi import FastAPI
from pydantic import BaseModel
import os
import json

app = FastAPI()
FILE = "puntaje.json"

class Puntaje(BaseModel):
    puntaje: int

@app.get("/")
async def root():
    return {"mensaje": "API de puntajes funcionando. Usa /puntaje"}

@app.post("/puntaje")
async def guardar_puntaje(data: Puntaje):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data.dict(), f, indent=4)
    return {"status": "ok"}

@app.get("/puntaje")
async def obtener_puntaje():
    if not os.path.exists(FILE):
        return {"puntaje": 0}
    
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
