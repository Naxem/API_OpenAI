from flask import Flask, render_template, request
from function.chatgpt import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/choix_ia/<int:choix>', methods=['POST'])
def choix_ia(choix):
    if choix == 1:
        choix = "choix 1"
    elif choix == 2:
        start_assisant(2)
        print("Success: start Chat GPT4")
    elif choix == 3:
        choix = "choix 3"
    else:
        choix = "erreur: pas de corespondance dans la liste de choix"
    return render_template('prompt.html')

if __name__ == '__main__':
    app.run(debug=True)