import sys
from bs4 import BeautifulSoup
import random
import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template(os.path.join("version2", "templates", "index.html"))

@app.route('/result', methods=['POST'])
def result():
    resposta1 = request.form['resposta1']
    resposta2 = request.form['resposta2']
    resposta3 = request.form['resposta3']
    return render_template('result.html', resposta1=resposta1, resposta2=resposta2, resposta3=resposta3)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
