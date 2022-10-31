import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import numpy as np



def getting_all_info_web_scraping(url):

    places_list = []

    for page in range(1,9):
        html = requests.get(f"{url}" + str(page))
        soup = BeautifulSoup(html.content, "html.parser")
        name_offering = soup.find_all("p", attrs={"class":"style_title__NcI0n"})

        for i in range(len(name_offering)):
            name_offering[i].getText()
            places_list.append(name_offering)
    
    return places_list[1]

    pricing_list = []

    for page in range(1,9):
        html = requests.get(f"{url}" + str(page))
        soup = BeautifulSoup(html.content, "html.parser")
        price_offering = soup.find_all("p", attrs={"class":"style_pricing__TKbkD"})

        for i in range(len(price_offering)):
            price_offering[i].getText()
            pricing_list.append(price_offering)

    return pricing_list[1]

    size_list = []

    for page in range(1,9):
        html = requests.get(f"{url}" + str(page))
        soup = BeautifulSoup(html.content, "html.parser")
        size_offering = soup.find_all("span", attrs={"class":"style_squarefeet__q7bHB"})

        for i in range(len(size_offering)):
            size_offering[i].getText()
            size_list.append(size_offering)
    return size_list[1]

    occupancy_list = []

    for page in range(1,9):
        html = requests.get(f"{url}" + str(page))
        soup = BeautifulSoup(html.content, "html.parser")
        occ_offering = soup.find_all("span", attrs={"class":"style_maxOccupancy__uKsmM"})

        for i in range(len(occ_offering)):
            occ_offering[i].getText()
            occupancy_list.append(occ_offering)


    return occupancy_list  


def address_info(url):
    places_list = []

    for page in range(1,9):
        html = requests.get(f"{url}" + str(page))
        soup = BeautifulSoup(html.content, "html.parser")
        name_offering = soup.find_all("p", attrs={"class":"style_title__NcI0n"})

        for i in range(len(name_offering)):
            name_offering[i].getText()
            places_list.append(name_offering)

    
    empty_list_places = []

    for i in places_list:
        for item in i:
            empty_list_places.append(item)
 


    places_list2 = []

    for i in empty_list_places:
        only_address = i.getText()
        places_list2.append(only_address)
    return places_list2


def pricing_info(url):
    
    pricing_list = []

    for page in range(1,9):
        html = requests.get(f"{url}" + str(page))
        soup = BeautifulSoup(html.content, "html.parser")
        price_offering = soup.find_all("p", attrs={"class":"style_pricing__TKbkD"})

        for i in range(len(price_offering)):
            price_offering[i].getText()
            pricing_list.append(price_offering)

    empty_list_price = []

    for i in pricing_list:
        for item in i:
            empty_list_price.append(item)

    pricing_list2 = []

    for i in empty_list_price:
        only_prices = i.getText().strip()
        if "$" in only_prices:
            pricing_list2.append(only_prices)
        else:
            pricing_list2.append("To ask")

    pricing_list3 = []

    for i in pricing_list2:
        pricing_list3.append(i[:7])

    pricing_list4 = []

    for i in pricing_list3:
        if "$":
            pricing_list4.append(i.replace("$","").replace(",",""))
        else:
            pricing_list4.append
    return pricing_list4


def site_size_info(url):
    size_list = []

    for page in range(1,9):
        html = requests.get(f"{url}" + str(page))
        soup = BeautifulSoup(html.content, "html.parser")
        size_offering = soup.find_all("span", attrs={"class":"style_squarefeet__q7bHB"})

        for i in range(len(size_offering)):
            size_offering[i].getText()
            size_list.append(size_offering)

    empty_list_size = []

    for i in size_list:
        for item in i:
            empty_list_size.append(item)

    size_list2 = []

    for i in empty_list_size:
        only_sizes = i.getText()
        size_list2.append(only_sizes[:6])
    return size_list2


def site_max_occupancy(url):
    occupancy_list = []

    for page in range(1,9):
        html = requests.get(f"{url}" + str(page))
        soup = BeautifulSoup(html.content, "html.parser")
        occ_offering = soup.find_all("span", attrs={"class":"style_maxOccupancy__uKsmM"})

        for i in range(len(occ_offering)):
            occ_offering[i].getText()
            occupancy_list.append(occ_offering)

    empty_list_occ = []

    for i in occupancy_list:
        for item in i:
            empty_list_occ.append(item)

    occupancy_list2 = []

    for i in empty_list_occ:
        only_occ = i.getText()
        occupancy_list2.append(only_occ[1:])
    return occupancy_list2

    