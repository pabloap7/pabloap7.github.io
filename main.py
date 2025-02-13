from data.database import database
from data.modelo.director import Director
from data.dao.dao_directores import DaoDirectores

from typing import Annotated

from typing import Union

from fastapi import FastAPI, Request, Form


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/directores")
def get_directores(request: Request, nombre: str = "pepe", otro: int = 1):
    directores = DaoDirectores().get_all(database)
    return templates.TemplateResponse(
        request=request, name="directores.html", context={"directores": directores, "nombre": nombre}
    )

@app.post("/add_director", response_class=HTMLResponse)
def add_director(request: Request, nombre: Annotated[str, Form()]):
    DaoDirectores().add_director(database, nombre)
    directores = DaoDirectores().get_all(database)
    return templates.TemplateResponse(
        "directores.html", {"request": request, "directores": directores}
    )

@app.post("/delete_director", response_class=HTMLResponse)
def delete_director(request: Request, id: Annotated[int, Form()]):
    DaoDirectores().delete_director(database, id)
    directores = DaoDirectores().get_all(database)
    return templates.TemplateResponse(
        "directores.html", {"request": request, "directores": directores}
    )

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/fincher", response_class=HTMLResponse)
async def fincher(request: Request):
     return templates.TemplateResponse(
         request=request, name="fincher.html"                                                    
     )

@app.get("/scorsese", response_class=HTMLResponse)
async def scorsese(request: Request):
     return templates.TemplateResponse(
         request=request, name="scorsese.html"                                                    
     )

@app.get("/tarantino", response_class=HTMLResponse)
async def tarantino(request: Request):
     return templates.TemplateResponse(
         request=request, name="tarantino.html"                                                    
     )

@app.get("/villeneuve", response_class=HTMLResponse)
async def villenueve(request: Request):
     return templates.TemplateResponse(
         request=request, name="villeneuve.html"                                                    
     )

@app.get("/spielberg", response_class=HTMLResponse)
async def spielberg(request: Request):
     return templates.TemplateResponse(
         request=request, name="spielberg.html"                                                    
     )

@app.get("/coppola", response_class=HTMLResponse)
async def coppola(request: Request):
     return templates.TemplateResponse(
         request=request, name="coppola.html"                                                    
     )