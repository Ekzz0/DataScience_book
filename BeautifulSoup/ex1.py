from bs4 import BeautifulSoup
import requests
url = "тут обычно пишут url сайта для парсинга"
html = requests.get(url).text  # html запрос на сайт и получение его кода
soup = BeautifulSoup(html, 'html5lib')

# Далее, с этим соупом можно работать:
# Чтобы найти нужный тег:
first_paragraph = soup.find('p')  # или soup.p
# Получим текстовое значение тега и разобьем его на части
first_paragraph_text = soup.p.text.split()
# Атрибуты тега можно извлечь:
first_paragraph_id = soup.p.get('id')
# Можно получить сразу несколько тэгов:
all_paragraphs = soup.find_all('p')  # или soup('p')
paragraphs_with_id = [p for p in soup('p') if p.get('id')]  # p.get('') возвращает None, если ничего нет
# Можно найти теги с конкретным классом стилевой таблицы
important_paragraphs = [p for p in soup('p') if 'important' in p.get('class', [])]
