import requests
from bs4 import BeautifulSoup

def importer(link_in):  # vai para o site da ufmg e gera um arquivo .txt com o nome do curso selecionado, todas as matérias presentes nele e um resumo de cada matéria
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
        nome_arquivo_saida = arquivo_entrada.readline().strip().replace(
            " ", "_").replace("/", "_") + ".txt"
        # abre o arquivo de saída
        with open("arquivos/" + nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
            # lê cada linha do arquivo de entrada a partir da segunda linha
            arquivo_saida.write(f"{arquivo_entrada.readline().strip()}\n")
            for linha in arquivo_entrada:
                # remove tudo antes do caractere "-" e o espaço subsequente
                linha = linha.split("- ", 1)[-1]
                if not " II" in linha.split(":")[0].split(":")[0] and not " IV" in linha.split(":")[0] and not " VI" in linha.split(":")[0]:  # desconsidera duplicatas
                    if linha.strip():
                        # escreve a linha no arquivo de saída
                        arquivo_saida.write(linha)


