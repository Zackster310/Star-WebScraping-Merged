import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = requests.get(url)

def scrape():
    name = []
    distance = []
    mass = []
    radius = []
    luminosity = []

    soup = BeautifulSoup(browser.text , "html.parser")

    table = soup.find('table')

    temp_list = []

    tr_tags = table.find_all('tr')

    for tr in tr_tags:
        td = tr.find_all('td')
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)

    for i in range(1, len(temp_list)):
        name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])
        luminosity.append(temp_list[i][7])

    df = pd.DataFrame(list(zip(name, distance, mass, radius, luminosity)), columns = ['star_name', 'distance', 'mass', 'radius', 'luminosity'])
    df.to_csv('bright_stars.csv')

scrape()