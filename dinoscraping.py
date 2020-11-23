#This file will stract data from https://en.wikipedia.org/wiki/List_of_dinosaur_genera and then create a list with allthe names of dinosaurs.
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import re

"""
#URL to scrap
url = 'https://en.wikipedia.org/wiki/List_of_dinosaur_genera'

#We scrap to get the list of names before we acces to every article
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')

#Then we obtain the URL and name of each dinosaur.
urls = soup.find_all('a', href=True)

#We create a tuple like this: (url, name). Unfortunately this way we will obtain undesired elements
links_and_names = [(url['href'], url.text) for url in urls]

#Then we eliminate all the elements don't have any relation with the dinosaurs
dino_data_clean = [links_and_names[link] for link in range(len(links_and_names)) if links_and_names[link][0].startswith("/wiki/")]

#Last elements are URLs to different officiall sites to wikipedia, nothing the matter for dinosaurs 
dino_data_clean = dino_data_clean[:2317:]

#Then we eliminate those tuples with blanks in the "name" element of the tuple, these exist because there are some images and the links_and_names store them because the "link" element exists.
#The most efiicient way to do it is by converting to a Data Frame and the turn it into a dictionary, this way we also eliminate posibly duplicated information.

dino_df = pd.DataFrame(dino_data_clean, columns = ['url', 'dinosaur'])
#We replace the '' Values for NaN numpy values
dino_df['dinosaur'] = dino_df['dinosaur'].replace('', np.nan)
dino_df = dino_df.dropna(axis = 0, subset = ['dinosaur'])
dino_data_clean = dino_df.set_index('url')['dinosaur'].to_dict()

#Now we get the final real urls and names of dinosaurs as a tuple
dino_data = [('https://en.wikipedia.org'+ url, dinosaur) for url, dinosaur in dino_data_clean.items()]

#The first 33 elements are uselees for us, they're wikipedia links let's erase them
dino_data = dino_data[33::]

#Also it's going to be usefull for us to have a list of urls to scrap, so:
dino_urls = [element for pair in dino_data for element in pair if element.startswith('https://en.wikipedia.org')]

#Now let's scrap every url looking for the first paragraph
dino_info = []

#This a varible i used to print progress of my scraping, totally useless for other porpuse
progress = 0

#We iterate throug all the urls in dino_urls
for url in range(len(dino_urls)):
    html = requests.get(dino_urls[url])
    soup = BeautifulSoup(html.text, 'lxml')
    paragraphs = soup.select('p')
    
    #first we get all paragraphs from the article using .text and strip() to clean the text.
    clean_paragraphs = [paragraph.text.strip() for paragraph in paragraphs]
    
    #The we use slicing list to get the first 4 paragraphs hoping the real 1st paragraph is there. Fortunatelly after running this script we had successs.
    clean_paragraphs = clean_paragraphs[:4:]


    #We append every paragraph to a list of paragraphs
    dino_info.append(' '.join(clean_paragraphs))
    progress += 1
    print(f'{(progress*100)/len(dino_urls)}%')

#An important Note about the following 3 lines of code: Lately I found that I can convert my two list into a single dictionary by using something like: dino_dict = {'URL': url, 'Dinosaur': dinosaur, 'Info':data_info} I didn't this because I would have to re scrap all pages and it takes like 40 minutes to my computer.
#First we create a DataFrame from the list o tuples called dino_data
dino_df = pd.DataFrame(dino_data, columns = ['URL','Dinosaur'])
#Then we create another DataFrame with all paragraphs we scrape from every single dinosaur article
dino_details = pd.DataFrame(dino_info, columns = ['Info'])
#Finally, we concatenate both DataFrames, so we have all the info into a single DataFrame
dino_df = pd.concat([dino_df, dino_details], ignore_index = True, axis = 1)

file_name = 'Dino_data.xlsx'

#Then I convert all my data into a Excel File so i can read, manipulate and clean my data from here instead of make the whole scrap over and over again.
dino_df.to_excel(file_name)
print('DataFrame is written to Excel File successfully!')
"""

"""Ok, from this point I will comment everythig in above so I don't have to scrap and I will create a new DataFrame from the excel file I create, this way everything will be we much more fast"""

file_name = 'Dino_data.xlsx'
dino_df = pd.read_excel(file_name)
#The excel file brings an additional column for number of element wich we don't need. We dorp it.
dino_df.drop('Unnamed: 0', inplace = True, axis = 1)
dino_df.columns = ['URLs','Dinosaur','Info']

dino_info = dino_df['Info'].to_dict()
dino_info = dino_info.values()
heights = []
progress = 0

#Next lines will find the height of every dinosaur
for element in dino_info:
    if re.findall('\d+\smeters',element):
        height = re.findall('\d+\smeters', element)
        heights.append(height)

    else:
        heights.append(list('-'))
    progress += 1 

heights_clean = []
for element in heights:
    for height in enumerate(element):
        if height[0] == 0:
            heights_clean.append(height[1])

"""for height in heights_clean:
    print(height)
    time.sleep(0.05)"""

#Next lines will find the weight
weights = []
for element in dino_info:
    if re.findall('\d+\stonnes|\d+\skilograms',element):
        weight = re.findall('\d+\stonnes|\d+\skilograms', element)
        weights.append(weight)

    else:
        weights.append(list('-'))

weights_clean = []
for element in weights:
    for weight in enumerate(element):
        if weight[0] == 0:
            weights_clean.append(weight[1])

dino_df.drop('Info', inplace = True, axis = 1)
heights_df = pd.DataFrame(heights_clean, columns = ['Height'])
weights_df = pd.DataFrame(weights_clean , columns = ['Weight'])
dino_df = pd.concat([dino_df, heights_df, weights_df], ignore_index = True, axis = 1) 
dino_df.columns = ['URL','Dinosaur','Height','Weight']
print(dino_df)
file_name = 'Dino_data.csv'
dino_df.to_csv(file_name)
print('DataFrame successfully exported to CSV file!')
