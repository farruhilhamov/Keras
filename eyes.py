import eyed3
import requests as rq
from  bs4 import BeautifulSoup as bs 
# audiofile = eyed3.load("i10.mp3")
# print(audiofile)

url = 'https://www.gazeta.uz/ru/'
raw = rq.get(url).text
soup = bs(raw)
text = soup.find_all('p')
texts = [str(s) for s in text]

print(type(texts))
print(len(texts))
# print(soup.find_all('p'))
# print(type(soup.find_all('p')))
# print(len(soup.find_all('p')))
