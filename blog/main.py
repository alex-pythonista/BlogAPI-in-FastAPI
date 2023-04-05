from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel
from .schemas import Blog

app = FastAPI()




@app.post('/blog')
def create(blog: Blog):
    return blog