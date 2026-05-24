from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Mi API en Cloud Run",
    description="API de ejemplo desplegada en Google Cloud Run con CI/CD",
    version="1.0.0"
)


# ── Modelos ──────────────────────────────────────────────────────────────────

class Item(BaseModel):
    nombre: str
    precio: float
    disponible: bool = True


# ── Endpoints ────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"mensaje": "¡Hola desde Cloud Run! 🚀 usar python se me hizo fácil"}

