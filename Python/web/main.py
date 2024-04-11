from flask import Flask, render_template, request
import openai
from config.key import key
from function.chatgpt import *

app = Flask(__name__)
openai.api_key = key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/choix_ia/<int:choix>', methods=['POST'])
def choix_ia(choix):
    if choix == 1:
        chat_gpt_text()
    elif choix == 2:
        choix = "ok2"
    elif choix == 3:
        choix = "choix 3"
    else:
        choix = "erreur: pas de corespondance dans la liste de choix"
    return choix

if __name__ == '__main__':
    app.run(debug=True)
    
    
def chat_gpt_text():
    
    start_assisant(2)
    