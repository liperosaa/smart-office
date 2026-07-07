from fastapi import FastAPI

app = FastAPI(
    title="Smart Office API",
    description="Sistema de gestão empresarial com Inteligência Artificial e Automação",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "Smart Office",
        "version": "1.0.0",
        "status": "online",
        "developer": "Felipe Padson"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }