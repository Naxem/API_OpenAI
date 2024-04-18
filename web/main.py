from flask import Flask, render_template, request
from function.chatgpt import *
from function.dallE import dallE

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/choix_ia/<int:choix>', methods=['POST'])
def choix_ia(choix):
    if choix == 1:
        print("Success: start Dall-e")
        return render_template('prompt.html')
    elif choix == 2:
        start_assisant(2)
        print("Success: start Chat GPT4")
        return render_template('prompt.html')
    else:
        choix = "erreur: pas de corespondance dans la liste de choix"
        return choix

@app.route('/chatgpt/<string:msg>', methods=['POST'])
def chatgpt(msg):
    create_message(msg)
    result = chatgptF()
    return render_template('result_chatgpt.html', result=result)
    
@app.route('/dallE/<string:msg>', methods=['POST'])
def dall_E(msg):
    result = dallE(msg)
    return render_template('result_dallE.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)