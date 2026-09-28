from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app=FastAPI()
templates=Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request':request})

@app.post('/process')
def process(task:str=Form(...), text:str=Form(...)):
    if task=='qna': return {'result':answer_question(text)}
    if task=='explain': return {'result':explain_topic(text)}
    if task=='quiz': return {'result':generate_quiz(text)}
    if task=='summary': return {'result':summarize_text(text)}
    return {'result':get_learning_recommendations(text)}
