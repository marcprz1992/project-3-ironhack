import requests
from pymongo import MongoClient
from pymongo import GEOSPHERE
import pandas as pd
import json
import os
import requests
import json
from dotenv import load_dotenv
import pandas as pd
import geopandas as gpd
from cartoframes.viz import Map, Layer, popup_element
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
import geopy
from geopy import distance 
import math
import os
import requests
import json
from dotenv import load_dotenv
import pandas as pd
import geopandas as gpd
from cartoframes.viz import Map, Layer, popup_element


def get_airports_from_foursquare (category_id, location, limit=50):
    if load_dotenv():
        token_fsq = os.getenv("API_Key")
        ll = f"{location[1]}%2C{location[0]}"
        url = f"https://api.foursquare.com/v3/places/search?categories={category_id}&ll={ll}&limit={str(limit)}&radius=25000"

        headers = {
            "accept": "application/json",
            "Authorization": token_fsq,
        }

        response = requests.get(url, headers=headers).json()

        return response
    else:
        print("There is no possible to run this function,you might be missing any required parameter")


def list_with_airports():
    def get_airports_from_foursquare (category_id, location, limit=50):
        if load_dotenv():
            token_fsq = os.getenv("API_Key")
            ll = f"{location[1]}%2C{location[0]}"
            url = f"https://api.foursquare.com/v3/places/search?categories={category_id}&ll={ll}&limit={str(limit)}&radius=25000"

            headers = {
                "accept": "application/json",
                "Authorization": token_fsq,
            }

            response = requests.get(url, headers=headers).json()

            return response
    
    new_list = []
    for i in response["results"]:

        name = i["name"]
        address =  i["location"]["formatted_address"]
        lat = i["geocodes"]["main"]["latitude"]
        lon = i["geocodes"]["main"]["longitude"]

        type_ = {"typepoint": 
                              {"type": "Point", 
                               "coordinates": [lat, lon]}}

        new_list.append({"name":name, "lat":lat, "lon":lon, "type":type_})

    return new_list


def get_starbucks_from_foursquare (query, location, limit=50):
    if load_dotenv():
        token_fsq = os.getenv("API_Key")   
        ll = f"{location[1]}%2C{location[0]}"
        url = f"https://api.foursquare.com/v3/places/search?query={query}&ll={ll}&limit={str(limit)}&&radius=1000"

        headers = {
            "accept": "application/json",
            "Authorization": token_fsq,
        }

        response = requests.get(url, headers=headers).json()

        return response

    else:
        print("There is no possible to run this function,you might be missing any required parameter")


def list_with_starbucks():

    def get_starbucks_from_foursquare (query, location, limit=50):
        if load_dotenv():
            token_fsq = os.getenv("API_Key")   
            ll = f"{location[1]}%2C{location[0]}"
            url = f"https://api.foursquare.com/v3/places/search?query={query}&ll={ll}&limit={str(limit)}&&radius=1000"

            headers = {
                "accept": "application/json",
                "Authorization": token_fsq,
            }

            response = requests.get(url, headers=headers).json()

            return response

        else:
            print("There is no possible to run this function,you might be missing any required parameter")




    starbucks_list = []
    for i in response["results"]:

        name = i["name"]
        address =  i["location"]["formatted_address"]
        lat = i["geocodes"]["main"]["latitude"]
        lon = i["geocodes"]["main"]["longitude"]

        type_ = {"typepoint": 
                              {"type": "Point", 
                               "coordinates": [lat, lon]}}

        starbucks_list.append({"name":name, "lat":lat, "lon":lon, "type":type_})

    return starbucks_list


def get_vegan_rest_from_foursquare (category_id, location, limit=50):
    if load_dotenv():
        token_fsq = os.getenv("API_Key")  
       
        ll = f"{location[1]}%2C{location[0]}"
        url = f"https://api.foursquare.com/v3/places/search?categories={category_id}&ll={ll}&limit={str(limit)}&&radius=3000"

        headers = {
            "accept": "application/json",
            "Authorization": token_fsq,
        }

        response = requests.get(url, headers=headers).json()
    
        return response
    else:
        print("There is no possible to run this function,you might be missing any required parameter")


def list_of_vegan_restaurants():
    def get_vegan_rest_from_foursquare (category_id, location, limit=50):
        if load_dotenv():
            token_fsq = os.getenv("API_Key")  

            ll = f"{location[1]}%2C{location[0]}"
            url = f"https://api.foursquare.com/v3/places/search?categories={category_id}&ll={ll}&limit={str(limit)}&&radius=3000"

            headers = {
                "accept": "application/json",
                "Authorization": token_fsq,
            }

            response = requests.get(url, headers=headers).json()

            return response
        else:
            print("There is no possible to run this function,you might be missing any required parameter")
    

    vegan_list = []
    for i in response["results"]:

        name = i["name"]
        address =  i["location"]["formatted_address"]
        lat = i["geocodes"]["main"]["latitude"]
        lon = i["geocodes"]["main"]["longitude"]

        type_ = {"typepoint": 
                              {"type": "Point", 
                               "coordinates": [lat, lon]}}

        vegan_list.append({"name":name, "lat":lat, "lon":lon, "type":type_})

    vegan_list


def get_pets_from_foursquare (category_id, location, limit=50):
    if load_dotenv():
        token_fsq = os.getenv("API_Key")    
        ll = f"{location[1]}%2C{location[0]}"
        url = f"https://api.foursquare.com/v3/places/search?categories={category_id}&ll={ll}&limit={str(limit)}&&radius=3000"

        headers = {
            "accept": "application/json",
            "Authorization": token_fsq,
        }

        response = requests.get(url, headers=headers).json()

        return response
    else:
        print("There is no possible to run this function,you might be missing any required parameter")        


def list_of_pet_grooming_places():
    def get_pets_from_foursquare (category_id, location, limit=50):
        if load_dotenv():
            token_fsq = os.getenv("API_Key")    
            ll = f"{location[1]}%2C{location[0]}"
            url = f"https://api.foursquare.com/v3/places/search?categories={category_id}&ll={ll}&limit={str(limit)}&&radius=3000"

            headers = {
                "accept": "application/json",
                "Authorization": token_fsq,
            }

            response = requests.get(url, headers=headers).json()

            return response
        else:
            print("There is no possible to run this function,you might be missing any required parameter")      
    

    pet_list = []
    for i in response["results"]:

        name = i["name"]
        address =  i["location"]["formatted_address"]
        lat = i["geocodes"]["main"]["latitude"]
        lon = i["geocodes"]["main"]["longitude"]

        type_ = {"typepoint": 
                              {"type": "Point", 
                               "coordinates": [lat, lon]}}

        pet_list.append({"name":name, "lat":lat, "lon":lon, "type":type_})

    return pet_list


def get_stadiums_from_foursquare (category_id, location, limit=20):
    if load_dotenv():
        token_fsq = os.getenv("API_Key") 
       
        ll = f"{location[1]}%2C{location[0]}"
        url = f"https://api.foursquare.com/v3/places/search?categories={category_id}&ll={ll}&limit={str(limit)}&&radius=10000"

        headers = {
            "accept": "application/json",
            "Authorization": token_fsq,
        }

        response = requests.get(url, headers=headers).json()

        return response
    else:
        print("There is no possible to run this function,you might be missing any required parameter")  


def list_of_stadiums():
    def get_stadiums_from_foursquare (category_id, location, limit=20):
        if load_dotenv():
            token_fsq = os.getenv("API_Key") 

            ll = f"{location[1]}%2C{location[0]}"
            url = f"https://api.foursquare.com/v3/places/search?categories={category_id}&ll={ll}&limit={str(limit)}&&radius=10000"

            headers = {
                "accept": "application/json",
                "Authorization": token_fsq,
            }

            response = requests.get(url, headers=headers).json()

            return response
        else:
            print("There is no possible to run this function,you might be missing any required parameter")     
    

    stadium_list = []
    for i in response["results"]:

        name = i["name"]
        address =  i["location"]["formatted_address"]
        lat = i["geocodes"]["main"]["latitude"]
        lon = i["geocodes"]["main"]["longitude"]

        type_ = {"typepoint": 
                              {"type": "Point", 
                               "coordinates": [lat, lon]}}

        stadium_list.append({"name":name, "lat":lat, "lon":lon, "type":type_})

    return stadium_list


def geometry_of_lists(list):
    df = pd.DataFrame(list)
    df2 = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["lon"], df["lat"]))
    return df2


def map_with_venues(df,category):
    the_map = Map(Layer(df, "color:black", popup_hover=[popup_element("name", f"{category} places")]))
    return the_map



