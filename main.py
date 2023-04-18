from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse

from models import Chat_Answer

import openai
import key
import sys


chatGPT_try = FastAPI()
templates = Jinja2Templates(directory="templates")

"""
@chatGPT_try.get("/")
def index(answer: Chat_Answer, request: Request):
    return templates.TemplateResponse("content.html", {
        "answer": answer.chat_answer,
        "request": request
    })
"""

@chatGPT_try.get("/")
def index():

    openai.organization = key.SK
    openai.api_key = key.AK

    message = "美味しいの意味を教えてください。"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
        ]
    )

    #print(response["choices"][0]["message"]["content"])

    return response["choices"][0]["message"]["content"]

if __name__ == '__main__':
    uvicorn.run(chatGPT_try)

