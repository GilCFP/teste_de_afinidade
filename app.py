from bs4 import BeautifulSoup
import random
import os
import requests
from flask import Flask, render_template, request, jsonify
#TODO BUG: CURSO PRECISA SER GLOBAL E SER ALTERADO COMO PELA FUNÇÃO, PORÉM QUANDO ISSO ACONTECE NO PRÓXIMO USO ELE FICA SO COM 2 DE LENGHT, CAUSANDO ERRO DE INDEX
curso = [None] * 6
total = [None] * 6
def dictgenerator():  # gera um dicionário com todos os cursos da UFMG como key direcionando ao site do respectivo curso
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


def importer(link_in):  # vai para o site da ufmg e gera um arquivo .txt com o nome do curso selecionado, todas as matérias presentes nele e um resumo de cada matéria
    print("Gerando base de dados(Isso pode demorar um pouco)...")
    page = requests.get(link_in)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("h1", class_="main__title")
    links = soup.find_all("a", class_="drop__link--underlined")
    with open("arquivos/input.txt", "w",encoding="utf-8") as output:
        output.write(title.text + "\n")
        for link in links:
            subject_url = "https://ufmg.br" + link["href"]
            subject_page = requests.get(subject_url)
            subject_soup = BeautifulSoup(subject_page.content, "html.parser")
            widget = subject_soup.find("div", class_="widget")
            first_paragraph = widget.find("p")
            first_paragraph = first_paragraph.text.replace("\n", " ")
            output.write(link.text + ": " + first_paragraph + "\n")
    with open("arquivos/input.txt", "r",encoding="utf-8") as arquivo_entrada:
        # lê a primeira linha do arquivo de entrada
        nome_arquivo_saida = arquivo_entrada.readline().strip().replace(
            " ", "_").replace("/", "_") + ".txt"
        # abre o arquivo de saída
        with open("arquivos/" + nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
            # lê cada linha do arquivo de entrada a partir da segunda linha
            arquivo_saida.write(f"{arquivo_entrada.readline().strip()}\n")
            for linha in arquivo_entrada:
                # remove tudo antes do caractere "-" e o espaço subsequente
                linha = linha.split("- ", 1)[-1]
                if not " II" in linha.split(":")[0][-3:] and not " IV" in linha.split(":")[0][-3:] and not " VI" in linha.split(":")[0][-3:]: #rdesconsidera duplicatas
                    if linha.strip():
                        # escreve a linha no arquivo de saída
                        arquivo_saida.write(linha)


def tester(arquivos, nomes):  # efetua o teste de afinidade para n cursos
    curso = [None] * arquivos
    for i in range(1, arquivos):
        curso[i - 1] = [None]
        curso[i - 1][0] = nomes[i]
    for i in range(0, len(curso) - 1):
        with open(curso[i][0], encoding="utf8") as data:
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
    questions = {}
    for i in range(0, len(curso) - 1):
        questions[curso[i][0].split("/")[1].replace(".txt", "")] = []
    for i in range(0, len(order)):
        questions[curso[order[i]][0].split("/")[1].replace(".txt", "")].append(curso[order[i]][results[order[i]][index[order[i]]]])
        index[order[i]] += 1
    return questions


app = Flask(__name__)
dic = dictgenerator()


@app.route('/', methods=['GET'])
def index():
    while len(curso) < 6:
        curso.append(None)
    for i in range(0,6):
        if curso[i] is not None:
            curso[i] = None
    return render_template("index.html", dict=dic, status=0)


@app.route('/result', methods=['POST'])
def result():
    for i in range(1, 6):
        curso[i] = request.form.get(f"curso{i}")
    for i in range(1, 6):
        j = i + 1
        while j < 6:
            if curso[i] == curso[j] and (curso[i] != None):
                return render_template("index.html", dict=dic, status=2)
            j += 1
    quantidade = 6
    for i in range(1, 6):
        if curso[i] == None:
            quantidade -= 1
    files = [None] * quantidade
    for i in range(1, quantidade):
        file_name = f"arquivos/{curso[i]}" + ".txt"
        if not os.path.isfile(file_name):
            importer(dic[curso[i]])
            files[i] = (f"arquivos/{curso[i]}.txt")
        else:
            files[i] = (f"arquivos/{curso[i]}.txt")
    # dicionário com uma key pra cada curso selecionado com o nome do respectivo
    questions = tester(quantidade, files)

    while None in curso:
        curso.remove(None)
    cursos = ["empty"] * len(curso)
    for i in range(0, len(curso)):
        cursos[i] = curso[i]
    return render_template("test.html", questions=questions, names=cursos)

@app.route('/test', methods=['POST'])
def test():     
    resultados = [0] * len(curso)
    for i in range(0,len(curso)):
        inputs = request.form.getlist(f"{curso[i]}")
        total[i] = len(inputs) * 5
        for j in range(0,len(inputs)):
            inputs[j] = int(inputs[j])
        resultados[i] = round(((sum(inputs)/total[i]) * 100),2)
    for i in range(0,len(curso)):
        curso[i]= curso[i].replace("_"," ")
    return render_template("result.html", resultados = resultados , curso = curso, max = len(curso))


    
    
    
if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
