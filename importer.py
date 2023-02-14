import requests
from bs4 import BeautifulSoup

url = "https://ufmg.br/cursos/graduacao/2379/91401"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
title = soup.find("h1", class_="main__title")
links = soup.find_all("a", class_="drop__link--underlined")
with open("input.txt","w") as output:
    output.write(title.text + "\n")
    for link in links:
        subject_url = "https://ufmg.br" + link["href"]
        subject_page = requests.get(subject_url)
        subject_soup = BeautifulSoup(subject_page.content, "html.parser")
        widget = subject_soup.find("div", class_="widget")
        first_paragraph = widget.find("p")
        first_paragraph = first_paragraph.text.replace("\n"," ")
        output.write(link.text + ": " + first_paragraph + "\n")
with open("arquivos/input.txt", "r") as arquivo_entrada:
    # lê a primeira linha do arquivo de entrada
    nome_arquivo_saida = arquivo_entrada.readline().strip() + ".txt"
    # abre o arquivo de saída
    with open("arquivos/" + nome_arquivo_saida.replace(" ","_"), "w") as arquivo_saida:
        # lê cada linha do arquivo de entrada a partir da segunda linha
        arquivo_saida.write(f"{arquivo_entrada.readline().strip()}\n")
        for linha in arquivo_entrada:
            # remove tudo antes do caractere "-" e o espaço subsequente
            linha = linha.split("- ", 1)[-1]
            if not "II" in linha and not "IV" in linha and not "VI" in linha:
                if linha.strip():
                    # escreve a linha no arquivo de saída
                    arquivo_saida.write(linha)



