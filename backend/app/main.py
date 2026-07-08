from fastapi import FastAPI
from app.routes.user_routes import router
from app.routes.room_routes import router as room_router


app = FastAPI(
    title="Smart Office API",
    version="1.0.0"
)

app.include_router(room_router)
app.include_router(router)


@app.get("/")
def home():

    return {
        "project": "Smart Office",
        "status": "online"
    }