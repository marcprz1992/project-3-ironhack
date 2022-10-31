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



def weighted_colleague(string):
    return (string/total_company)*100


def design_or_success_companies(database,coll_name):
    client = MongoClient("localhost:27017")
    db = client[(f"{database}")]
    c = db.get_collection(f"{coll_name}")
    
    condition_one = {"description": {"$regex": "design"}}
    condition_two = {"tag_list": {"$regex": "design"}}
    condition_three = {"name": {"$regex": "design"}}
    condition_four = {"category_code": {"$regex": "design"}}
    condition_five = {"total_money_raised": {"$regex": "M"}}
    condition_six = {"total_money_raised": {"$regex": "B"}}
    condition_seven = {}
    
    projection = {"name": 1, "number_of_employees": 1, "total_money_raised": 1,"offices.country_code": 1,"offices.city": 1, "_id":0}
    result_filtering = list(c.find({
    "$or": [
         condition_one,
          condition_two, condition_three,
            condition_four,
          condition_five,condition_six
    ], 
    "number_of_employees": {"$gte": 3000}
}, projection))
    return result_filtering


def calling_first_dataframe():
    df = pd.DataFrame(design_or_success_companies(database,coll_name))
    df["total_offices"] = df["offices"].apply(lambda x: len(x))
    df.sort_values(by="total_offices", ascending=False).reset_index().drop(['index'], axis=1)
    return df


def dictionary_of_cities(df):
    
    city_dict = {}
    for item, rows in df.iterrows():
        for i in rows["offices"]:
            ciudad = i["city"]
            if ciudad in city_dict.keys():
                city_dict[ciudad] +=1
            else:
                city_dict[ciudad]  =1
    {k: v for k, v in sorted(city_dict.items(), key=lambda item: item[1])}
    return city_dict


def dictionary_of_countries(df):
    country_dict = {}
    for item, rows in df.iterrows():
        for i in rows["offices"]:
            country = i["country_code"]
            if country in country_dict.keys():
                country_dict[country] +=1
            else:
                country_dict[country]  =1
    {k: v for k, v in sorted(country_dict.items(), key=lambda item: item[1])}
    country_dict


def companies_latandlong(a,b):
    client = MongoClient("localhost:27017")
    db = client[f"{a}"]
    c = db.get_collection(f"{b}")
    
    condition_one = {"description": {"$regex": "design"}}
    condition_two = {"tag_list": {"$regex": "design"}}
    condition_three = {"name": {"$regex": "design"}}
    condition_four = {"category_code": {"$regex": "design"}}
    condition_five = {"total_money_raised": {"$regex": "M"}}
    condition_six = {"total_money_raised": {"$regex": "B"}}
    condition_seven = {}

    projection = {"name": 1, "number_of_employees": 1, "total_money_raised": 1,"offices.country_code": 1,"offices.city": 1,"offices.latitude": 1,"offices.longitude": 1, "_id":0}
    result_filtering_latlong = list(c.find({
        "$or": [
             condition_one,
              condition_two, condition_three,
                condition_four,
              condition_five,condition_six
        ], 
        "number_of_employees": {"$gte": 3000}
    }, projection))


    return result_filtering_latlong


def companies_by_city(database,coll_name,city):
    client = MongoClient("localhost:27017")
    db = client[f"{database}"]
    c = db.get_collection(f"{coll_name}")
    
    condition_one = {"description": {"$regex": "design"}}
    condition_two = {"tag_list": {"$regex": "design"}}
    condition_three = {"name": {"$regex": "design"}}
    condition_four = {"category_code": {"$regex": "design"}}
    condition_five = {"total_money_raised": {"$regex": "M"}}
    condition_six = {"total_money_raised": {"$regex": "B"}}
    condition_seven = {"number_of_employees": {"$gte": 3000}}
    condition_eight = {"offices.city": {"$regex": f"{city}"}}
    
    projection = {"name": 1, "number_of_employees": 1, "total_money_raised": 1,"offices.country_code": 1,"offices.city": 1,"offices.latitude": 1,"offices.longitude": 1, "_id":0}
    result_filtering_latlong_nyc = list(c.find({
        "$and": [
            {
                "$or": [
                     condition_one,
                    condition_two, condition_three,
                    condition_four,
                      condition_five,condition_six
                        ]}, 

        condition_seven,condition_eight]}, projection))


    return result_filtering_latlong_nyc


def filtered_db_nyc(df,city):
    df2 = (df[df['city'] == f"{city}"]).reset_index().drop('index', axis=1) 
    df3 = df2[df2['latitude'].notna()]
    return df3


def getting_coordinates_from_offices(df):
    list = []

    for item, rows in df.iterrows():
        for i in rows["offices"]:
            list.append(i)

    return list


def dataframe_with_coordinates_by_city(list):
    table_with_coordinates = pd.DataFrame(list)
    return table_with_coordinates


def my_empty_map(lat,lon):
    map  = Map(location = [f"{lat}",f"{lon}"], zoom_start = 15)
    return map


def new_column_in_df():
    company = ['Company 1', 'Company 2', 'Company 3', 'Company 4','Company 5']
    df2 = df.copy()
    df2['Company'] = company
    return df2


def markers_for_df(df,map):

    for index, row in df.iterrows():

        #1. MARKER without icon
        location = {"location": [row["latitude"], row["longitude"]], "tooltip": row["Company"]}

        #2. Icon      
        icon = Icon (
                color="red",
                opacity = 0.6,
                prefix = "fa",
                icon="briefcase",
                icon_color = "black"
            )

        #3. Marker
        new_marker = Marker(**location, icon = icon, radius = 2)

        #4. Add the Marker
        new_marker.add_to(f"{map}")
        return map


def markers_for_df_with_conditions(df,map):
        for index, row in df.iterrows():
            

            #1. MARKER without icon
            venue = {"location": [row["lat"], row["lon"]], "tooltip": row["name"]}

            #2. Icon
            if row["category"] == "airport":        
                icon = Icon (
                    color="black",
                    opacity = 0.6,
                    prefix = "fa",
                    icon="plane",
                    icon_color = "white"
                )
            elif row["category"] == "starbucks":
                icon = Icon (
                    color="green",
                    opacity = 0.6,
                    prefix = "fa",
                    icon="coffee",
                    icon_color = "black"
                )
            elif row["category"] == "vegan":
                icon = Icon (
                    color="pink",
                    opacity = 0.6,
                    prefix = "fa",
                    icon="leaf",
                    icon_color = "black"
                )
            elif row["category"] == "petcare":
                icon = Icon (
                    color="gray",
                    opacity = 0.6,
                    prefix = "fa",
                    icon="paw",
                    icon_color = "black"
                )     
            else:
                icon = Icon (
                    color="orange",
                    opacity = 0.6,
                    prefix = "fa",
                    icon="futbol-o",
                    icon_color = "black",
                    icon_size=(14, 14)
                )
            #3. Marker
            new_marker = Marker(**venue, icon = icon, radius = 2)

            #4. Add the Marker
            new_marker.add_to(map)
            return map


def haversine(coord1, coord2):

    # Coordinates in decimal degrees (e.g. 2.89078, 12.79797)
    lon1, lat1 = coord1
    lon2, lat2 = coord2

    R = 6371000  # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in meters
    km = meters / 1000.0  # output distance in kilometers
    #return meters
    
    #meters = round(meters, 3)
    km = round(km, 1)
    return km
    
    #print(f"Distance: {meters} m")
    #print(f"Distance: {km} kilometres")‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍


def list_with_distances_to_a_coordinate(df):
    distance_list = []

    for item, rows in nyc_venues3.iterrows():
            coords_1 = (40.755716,-73.979247)
            coords_2 = (df["lat"][item],df["lon"][item])
            distance_trial = (geopy.distance.great_circle(coords_1, coords_2).km)
            final_distance_trial = round(distance_trial,1)
            final_distance_trial
            distance_list_2.append(final_distance_trial)

    return distance_list


def dataframe_with_distance_column_added(df):
    df2 = df.copy()
    df2['distance(km)'] = distance_list
    return df2



def calculating_average_distance(df):
    mean_distances = df.groupby("category")["distance(km)"].mean()
    return mean_distances


def type_point (list_):
    return {"type": "Point", "coordinates": list_}


def find_nyc_area (list_,database,collection):
    client = MongoClient("localhost:27017")
    db = client.get_database(f"{database}")
    collection = db.get_collection(f"{collection}")
    
    type_point_converted = type_point(list_)

    proy_ = {"name":1, "_id": 0}
    return collection.find_one({"geometry":
                        {"$geoIntersects": 
                            {"$geometry": type_point_converted}}}, proy_)


