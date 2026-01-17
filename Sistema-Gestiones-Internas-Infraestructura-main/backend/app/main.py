from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import me, gestiones, catalogos, usuarios

app = FastAPI(title="Infra Gestión API")

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^http://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(me.router)
app.include_router(catalogos.router)
app.include_router(gestiones.router)
app.include_router(usuarios.router)
