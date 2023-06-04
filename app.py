from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.routing import APIRouter
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(request: Request):
    # get the message from the form
    data = await request.form()
    # get the message from the form
    message = data.get("message")
    
    return templates.TemplateResponse("chat.html", {"request": request, "message": message})


@app.post("/bot_response/{message}")
async def chat_with_bot(request: Request, message: str):
    import random
    bot_responses = ["How aslkdlas alksdlkasd lkansdlka kalsdn loklasdl lknadl lkansda you?","How aslkdlas alksdlkasd lkansdlka kalsdn loklasdl lknadl lkansda you?", "How aslkdlas alksdlkasd lkansdlka kalsdn loklasdl lknadl lkansda you?", "I am fine", "Bye", "Goodbye"]
    message = random.choice(bot_responses)
    return {"message": message}