#This file will stract data from https://en.wikipedia.org/wiki/List_of_dinosaur_genera and then create a list with allthe names of dinosaurs.
import pandas as pd
import requests
from bs4 import BeautifulSoup

#URL to scrap
url = 'https://en.wikipedia.org/wiki/List_of_dinosaur_genera'

#We scrap to get the list of names before we acces to every article
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
dinosaurs = soup.select('i')
list_of_dinosaurs = [dinosaur.text for dinosaur in dinosaurs]
#print(list_of_dinosaurs)
print(len(list_of_dinosaurs))
exceptions = [' — possible junior synonym of ', ' – possible junior synonym of ', ' - possible synonym of ', ' - possibly non-dinosaurian', 'nomen nudum', ' - ', ' – a non-dinosaurian ', 'preoccupied', ' name, now known as ', ' – possibly ', '']
#The main problem in here is that we have this different exceptions tat we don't want to add to th liste fortunately, after the scraping we only have to delete the nomen nudum element and the duplicated elements.

#Eliminating the nomen nudum elements
for dinosaur in list_of_dinosaurs:
    if dinosaur == 'nomen nudum':
        list_of_dinosaurs.remove(dinosaur)
#print(len(list_of_dinosaurs))

#Eliminating the duplicated elements:
#clean_list_of_dinosaurs = [dinosaur for dinosaur in list_of_dinosaurs if dinosaur not in list_of_dinosaurs]
clean_list_of_dinosaurs = list(dict.fromkeys(list_of_dinosaurs))
#iprint(len(clean_list_of_dinosaurs))

#Then we obtain the URL of each dinosaur.
urls = soup.select('a')
urls_clean = [url.get('href') for url in urls]
print(urls_clean)
