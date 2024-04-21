import importlib
import pkgutil

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dynamically import all routers from the routes package
package_name = "routes"
package = importlib.import_module(package_name)
for _, module_name, _ in pkgutil.iter_modules(package.__path__):
    module = importlib.import_module(f"{package_name}.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router)


@app.get("/")
def read_root():
    return {"Welcome to": "GDSC's Hackathon project"}




