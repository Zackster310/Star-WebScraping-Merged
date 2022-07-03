import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = requests.get(url)

def scrape():
    name = []
    distance = []
    mass = []
    radius = []

    soup = BeautifulSoup(browser.text , "html.parser")

    table = soup.find_all('table')

    temp_list = []

    tr_tags = table[7].find_all('tr')

    for tr in tr_tags:
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)

    for i in range(1, len(temp_list)):
        name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])

    df = pd.DataFrame(list(zip(name, distance, mass, radius,)), columns = ['star_name', 'distance', 'mass', 'radius'])
    df.to_csv('dwarf_stars.csv')

scrape()