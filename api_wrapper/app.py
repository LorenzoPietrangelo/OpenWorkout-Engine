from fastapi import FastAPI

from api_wrapper.routers import catalogo, scheda

app = FastAPI(
    title="OpenWorkout Engine API",
    description="Genera schede di allenamento personalizzate.",
    version="1.0.0",
)

app.include_router(catalogo.router)
app.include_router(scheda.router)
