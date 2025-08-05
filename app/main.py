from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.database.db import Base, engine
from app.routes import user, book

# Creo las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


app.include_router(user.router)
app.include_router(book.router)
