import requests
from collections import Counter
from bs4 import BeautifulSoup as Soup

url = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D1%88%D0%B5%D0%BC%D0%B0%D1%8F#mw-pages"


next_page = True    # индикатор наличия активной ссылки "Следующая страница"
animals_counter = []

while next_page is True:
    html = requests.get(url)
    soup = Soup(html.text, 'html.parser')
    names = soup.find('div', class_='mw-category').find_all('a')
    for name in names:
        animals_counter.append(name.text[:1])
    links = soup.find('div', id='mw-pages').find_all('a')
    for link in links:
        if link.text == 'Следующая страница':
            url = 'https://ru.wikipedia.org/' + link.get('href')
            next_page = True
        else:
            next_page = False


def output():
    output = ""
    data = Counter(animals_counter)
    for key in data.keys():
        output += "{}: {}\n".format(key, data[key])
    return output


print(output())
