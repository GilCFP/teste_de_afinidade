import sys
from bs4 import BeautifulSoup
import random
import os
import requests
from flask import Flask, render_template, request
#TODO fazer com que o tester retorne um array com todas as matérias uma por linha , organiazdas de forma aleatória
#TODO implementar outra função chamada counter que vai contar a pontuação de cada curso
#TODO possivelmente usar divs com class com os nomes dos cursos pra que consiga contabilizar os pontos

def dictgenerator(): #gera um dicionário com todos os cursos da UFMG como key direcionando ao site do respectivo curso
    link = "https://ufmg.br/cursos/graduacao/"
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    list = soup.find_all("ol", class_="drop__list--depth-1")
    dic = {}
    i = 0
    for row in list:
        li = row.find_all("li", class_="drop__list-item")
        for element in li:

            name = element.find("a", class_="drop__link--accordion")
            if name != None:
                ol = element.find("ol", class_="drop__list")
                link = ol.find("a", class_="drop__link")
                name = name.text
                name = name.strip().replace(' ', '_')
                name = name.replace("/", "_")
                dic[name] = (f"https://ufmg.br{link['href']}")
                i += 0
    return dic
def importer(link_in): #vai para o site da ufmg e gera um arquivo .txt com o nome do curso selecionado, todas as matérias presentes nele e um resumo de cada matéria
    print("Gerando base de dados(Isso pode demorar um pouco)...")
    page = requests.get(link_in)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("h1", class_="main__title")
    links = soup.find_all("a", class_="drop__link--underlined")
    with open("arquivos/input.txt", "w") as output:
        output.write(title.text + "\n")
        for link in links:
            subject_url = "https://ufmg.br" + link["href"]
            subject_page = requests.get(subject_url)
            subject_soup = BeautifulSoup(subject_page.content, "html.parser")
            widget = subject_soup.find("div", class_="widget")
            first_paragraph = widget.find("p")
            first_paragraph = first_paragraph.text.replace("\n", " ")
            output.write(link.text + ": " + first_paragraph + "\n")
    with open("arquivos/input.txt", "r") as arquivo_entrada:
        # lê a primeira linha do arquivo de entrada
        nome_arquivo_saida = arquivo_entrada.readline().strip().replace(" ", "_") + ".txt"
        # abre o arquivo de saída
        with open("arquivos/" + nome_arquivo_saida, "w") as arquivo_saida:
            # lê cada linha do arquivo de entrada a partir da segunda linha
            arquivo_saida.write(f"{arquivo_entrada.readline().strip()}\n")
            for linha in arquivo_entrada:
                # remove tudo antes do caractere "-" e o espaço subsequente
                linha = linha.split("- ", 1)[-1]
                if not "II" in linha and not "IV" in linha and not "VI" in linha: #rdesconsidera duplicatas
                    if linha.strip():
                        # escreve a linha no arquivo de saída
                        arquivo_saida.write(linha)
def tester(arquivos, nomes): #efetua o teste de afinidade para n cursos
    curso = [None] * arquivos
    counter = [0] * arquivos
    for i in range(1, arquivos):
        curso[i - 1] = [None]
        curso[i - 1][0] = nomes[i]
    for i in range(0, len(curso) - 1):
        with open(curso[i][0]) as data:
            for row in data:
                curso[i].append(row)
    order = [0] * (len(curso[0]) - 1)
    for i in range(1, len(curso)-1):
        order += [i] * (len(curso[i]) - 1)
    random.shuffle(order)
    results = [None] * len(order)
    for i in range(0, len(curso)-1):
        results[i] = list(range(1, len(curso[i])))
        random.shuffle(results[i])
    index = [0] * len(curso)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i in range(0, len(order)):
        print(curso[order[i]][results[order[i]]
              [index[order[i]]]], end="\n\n\n\n")
        index[order[i]] += 1
        answer = "inicialized"
        while answer != "S" and answer != "N":
            answer = input("S para Sim e N para Não: ",)
        if answer == "S":
            counter[order[i]] += 1
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i in range(0, len(curso) - 1):
        print(f"{curso[i][0].split('.')[0].split('/')[1]}: {counter[i]} de {order.count(i)} Afinidade:{round(float(counter[i])/order.count(i)*100 , 2)}%")

app = Flask(__name__)
dic = dictgenerator()
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", dict = dic, status = 0)
@app.route('/result', methods=['POST'])
def result():
    curso = [None] * 6
    for i in range(1,6):
        curso[i] = request.form.get(f"curso{i}")
    for i in range(1,6):
        j = i + 1
        while j < 6:
            if curso[i] == curso[j] and (curso[i] != None):
                return render_template("index.html", dict = dic, status = 2)
            j +=1
    quantidade = 6
    for i in range (1,6):
        if curso[i] == None:
            quantidade -= 1
    print(curso[3], quantidade)
    files = [None] * quantidade
    for i in range(1, quantidade):
        file_name = f"arquivos/{curso[i]}" + ".txt"
        if not os.path.isfile(file_name):
            importer(dic[curso[i]])
            files[i] = (f"arquivos/{curso[i]}.txt")
        else:
            files[i] = (f"arquivos/{curso[i]}.txt")
    matérias = tester(quantidade,files)
    return render_template("index.html", dict = dic, status = 0)
    main()
    resposta1 = request.form['resposta1']
    resposta2 = request.form['resposta2']
    resposta3 = request.form['resposta3']
    return render_template('result.html', resposta1=resposta1, resposta2=resposta2, resposta3=resposta3)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
