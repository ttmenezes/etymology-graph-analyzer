import requests
import networkx as nx
from bs4 import BeautifulSoup

# get 1000 most common English words - source: https://gist.github.com/deekayen/4148741
wordsFile = open('most-common-eng-words.txt', 'r')
wordSet = list(wordsFile.read().splitlines())

# get langauges, families, and terms
termsFile = open('terms.txt', 'r')
termSet = list(termsFile.read().splitlines())

# make graph
G = nx.Graph()

for term in termSet:
    G.add_node(term, color='yellow')

# idea: family might (most times) be the word/s between 'from' and class tag "foreign notranslate"

for i in range(500):
    word = wordSet[i]
    ancestorData = requests.get("https://www.etymonline.com/word/" + word)

    ancestorSoup = BeautifulSoup(ancestorData.text, 'html.parser').find_all(
        style="position:relative")
    for excerpt in ancestorSoup:
        text = excerpt.get_text()
        for term in termSet:
            if term in text:
                G.add_edge(word, term)

    print(word)
    # print(ancestorSoup.find_all(class_="foreign"))

nx.write_gml(G, '500-most-common.gml')
