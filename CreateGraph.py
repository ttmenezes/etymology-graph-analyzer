import networkx as nx
import requests
import re
from bs4 import BeautifulSoup

# get 3000 most common English words
wordsiteData = requests.get(
    'https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/')
wordSoup = BeautifulSoup(wordsiteData.text, 'html.parser')
mostCommonEnglishWords = wordSoup.find_all('p')[11].get_text().split('\n\t')

# make graph
G = nx.Graph()

word = mostCommonEnglishWords[0]

# for word in mostCommonEnglishWords:

ancestorData = requests.get("https://www.etymonline.com/word/" + word)
siteText = ancestorData.text

# initialize words array and index array
words = siteText.split(" ")
# maps characters to the index of their word in the words array
lettersToWords = []
wordIndex = 0
for i in range(0, len(siteText)):
    if (siteText[i] == " "):
        wordIndex += 1
        lettersToWords.append(-1)
    else:
        lettersToWords.append(wordIndex)
print(siteText)

# for each match, trace backwards until language classification is found
# and trace forwards to find root word

for match in re.finditer('<span class="foreign notranslate">', siteText):
    span = match.span()
    startInd = span[0]
    endInd = span[1]

    # get ancestor word
    forwardProg = endInd
    while(siteText[forwardProg] != " " and siteText[forwardProg] != "<"):
        forwardProg += 1
    ancestorWord = siteText[endInd: forwardProg]
    print("here" + ancestorWord)

    # get ancestor word's family
    backProg = startInd
    # find latest group of words before the tag that start with a capital letter
    while(siteText[backProg].isupper() is False):
        backProg -= 1

    print(words[lettersToWords[backProg]])

    print(siteText[backProg])


# text = this.text()

# ss = ancestorSoup.find_all(class_="foreign notranslate")
# for tag in ss:
#     print(tag)
