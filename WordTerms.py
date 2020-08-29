import requests
from bs4 import BeautifulSoup

termsPage = requests.get('https://www.etymonline.com/columns/post/abbr?utm_source=etymonline_footer&utm_medium=link_exchange')

termSoup = BeautifulSoup(termsPage.text, 'html.parser')

termSet = set()

file1 = open('terms.txt', 'a')

for term in termSoup.find(class_="post__content--uwriH").find_all('strong'):
    word = term.get_text()
    if (word[0].istitle()):
        termSet.add(word)
        file1.write(word+ '\n')