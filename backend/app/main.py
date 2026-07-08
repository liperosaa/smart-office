from fastapi import FastAPI
from app.routes.user_routes import router
from app.routes.room_routes import router as room_router
from app.routes.equipment_routes import router as equipment_router
from app.routes.energy_routes import router as energy_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.report_routes import router as report_router

app = FastAPI(
    title="Smart Office API",
    version="1.0.0"
)

app.include_router(room_router)
app.include_router(equipment_router)
app.include_router(router)
app.include_router(energy_router)
app.include_router(dashboard_router)
app.include_router(report_router)


@app.get("/")
def home():

    return {
        "project": "Smart Office",
        "status": "online"
    }