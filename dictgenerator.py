import requests
from bs4 import BeautifulSoup

url = "https://ufmg.br/cursos/graduacao/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
list = soup.find_all("ol", class_="drop__list--depth-1")
out = {}
i = 0
for row in list:
    li = row.find_all("li", class_="drop__list-item")
    for element in li:

        name = element.find("a",class_="drop__link--accordion")
        if name != None:
            ol = element.find("ol",class_="drop__list")
            link= ol.find("a",class_="drop__link")
            name = name.text
            name = name.strip().replace(' ','_')
            out[name] = (f"https://ufmg.br{link['href']}")
print(out)
