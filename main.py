from fastapi import FastAPI

from src.rgb_lights_server import router

app = FastAPI(
    redoc_url=None,
    docs_url="/",
    title="RGB Lights control server",
    description="Many clients can connect to this server to sync RGB lights settings",
    version="1.0.0",
)


app.include_router(router.router)
