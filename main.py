from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

from utils import is_spam

app = FastAPI()


class SpamFilter(BaseModel):
    content: str
    spam_domains: List[str]
    depth: int


@app.get('/')
async def root():
    return {'message': "Hello World"}


@app.post('/spam-filter', response_model=bool)
async def spam_filter(
    request_body: SpamFilter
):
    return is_spam(**request_body.dict())
