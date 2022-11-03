# Choosing the best city for our new offfice

## Objective

As part of our Data Analytics bootcamp, we have been assigned the task of finding the best location across the globe for the - fake - company we work at, so we can put everything we have learned so far into practice.

In order to do that, the following tools have been used:

a) MongoDB - as the initial database with other companies information was coming from this data source

b) Foursquare API - to make our analysis richer and more robust

c) Real State web scraping - once the city & area we want to go after have been chosen, some web scraping has been done in order to find the perfect location for our new office

## Defining the main criteria

As part of this task, there were some criteria that we had to take into consideration in order to find the best spot for our company, such as:


1) Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.

2) 30% of the company staff have at least 1 child.

3) Developers like to be near successful tech startups that have raised at least 1 Million dollars.

4) Executives like Starbucks A LOT. Ensure there's a starbucks not too far.

5) Account managers need to travel a lot.

6) Everyone in the company is between 25 and 40, give them some place to go party.

7) The CEO is vegan.

8) If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.

9) The office dog - Dobby - needs a hairdresser every month. Ensure there's one not too far away.

Given the weight of each department within the company as well as some of the criterias being crucial for the business (please refer to [Main_code]([](Main_code.ipynb)) notebook to see the code details), the following criteria is what has been selected as key in order to find the best spot:

a) Companies that do anything related to design

b) Tech startups that are worth more than $1m 

c) Having Airports nearby

d) Having also Starbucks around

e) Vegan restaurants so our CEO can be happy :)

f) Pet Grooming places for Dobby

g) Some Basketball Stadiums and courts nearby


The first two criteria have become the starting point for this analysis, so the other criteria have been applied to the top 3 cities where criteria 1 and 2 were met.


## Choosing the key cities to explore

As per above, we got a good read from MongoDB via a company collection we had access to, so we could run some queries to filter the data by criteria 1 and 2. The following screenshot is an example of the output from this database:

![](Figures/screenshot1.png)

Now with a new column added with the addition of all the offices grouped by actual company:

![](Figures/screenshot2.png)

This information itself is not telling us much, so let's see if a dictionary summarising us the number of offices per city is giving us more insights:

![](Figures/screenshot3.png)

This seems more accurate! Let's see if this is also corresponding with the information by country:

![](Figures/screenshot4.png)

Okay - it seems to be! Given the current political inestability in Russia, let's focus our analysis in the US, especifically in New York, San Francisco & San Jose.

Before jumping onto the next section, we need to get the actual coordinates of the companies within those areas, so we can use those as point of reference to calculate distances. The below is an example of the information gathered for New York:

![](Figures/screenshot5.png)


## Gathering information from Foursquare API

Now that we have some coordinates to base our analysis on, we can explore the rest of the criteria pointed above. Let's start with the airports.

## 1) Airports

Using the first coordinate across the three cities as well as using the respective request codes from Foursquare API, we can get to the following output for the NYC airports:

![](Figures/screenshot6.png)

Similar for San Francisco:

![](Figures/screenshot7.png)

And for San Jose:

![](Figures/screenshot8.png)

## 2) Starbucks

Similar approach than for airports but this time to find the nearby Starbucks:

New York:

![](Figures/screenshot9.png)

San Francisco:

![](Figures/screenshot10.png)

San Jose:

![](Figures/screenshot11.png)

## 3) Vegan restaurants

New York:

![](Figures/screenshot12.png)

San Francisco:

![](Figures/screenshot13.png)

San Jose:

![](Figures/screenshot14.png)

## 4) Pet Grooming places

New York:

![](Figures/screenshot15.png)

San Francisco:

![](Figures/screenshot16.png)

San Jose:

![](Figures/screenshot17.png)

## 5) Basketball Stadiums

For this one, the actual basketball courts were also included as part of the analysis.

New York:

![](Figures/screenshot18.png)

San Francisco:

![](Figures/screenshot19.png)

San Jose:

![](Figures/screenshot20.png)

## Venues dataframe

Now that we have all the data needed, we can concatenate all the info so everything is together in three different pandas dataframes, one for each city:

New York:

![](Figures/screenshot21.png)

San Francisco:

![](Figures/screenshot22.png)

San Jose:

![](Figures/screenshot23.png)

## Plotting everything together

We can now plot all the venues within each city in a map to compare their location vs. the main companies we initially targeted so we can have a first guess on how far things are.

[New York map with venues](Maps/nyc_map_with_venues.html)

[San Francisco map with venues](Maps/sf_map_with_venues.html)

[San Jose map with venues](Maps/sj_map_with_venues.html)

## Calculating the actual distance

The information on the map is good if you want to check how many venues are nearby, but it's very difficult to get the actual distance vs. the first company's coordinates we took from each city.

Let's see if the distances using the "geopy" library help us make a decision as in which city we should go after:

New York:
![](Figures/screenshot24.png)

San Francisco:
![](Figures/screenshot25.png)

San Jose:
![](Figures/screenshot26.png)

Now we can see the distance between each venue and the coordinates of a given company within each city, but let's see what the average distance of each venue is for each city:

![](Figures/screenshot27.png)

As expected, the airport is what each company within each city has most distance with, but for the rest of the criteria New York seems to be pretty much the best location for our office, so that's where we are going to! 

## Web Scraping to support decision

Now that we know the city, we also need to look at what neighbourhood we want to establish our new office. Given the location of "Company 1" (the one used to get the coordinates) seems quite a good spot, let's see if we can also base ourselves there.

By using $geoIntersects on MongoDB NYC neighbourhoods collection, we are able to know the name of the area we want to be, which is Midtown-Midtown South Manhattan:

![](Figures/screenshot28.png)

Some web scraping has been done in the following [link](https://www.squarefoot.com/office-space/m/ny/new-york/635d40e4-ee2c-4144-8c95-040714888811?neighborhoods=88d9e668-b2fa-4ebe-a54e-488328f56823%2C487bd69c-8f9d-4441-895b-29d1d40afc17%2C82351707-ced7-4c44-aab6-f39347566197%2C5dc352b4-5a83-4b08-b1d7-bdd50fb85e79%2Ccde1e681-bff5-4c40-b96a-f5ba67354cfc%2Ce6657556-6c44-47e8-b825-f61d1a35896e%2C78edec76-bc46-4b67-8401-6697469f7fbd%2Cac7231b4-c3eb-4141-ad47-6799653ee1f2%2C94e3c05e-07b1-4ec2-9ce6-52de63e49ab0%2Cd6a095c6-cb75-4667-9b78-7ca8528498ee%2C7d2cfc8c-a753-449f-bb19-7054112af57e%2Cf5aa7229-00b5-42d8-9442-55f884ae1f3b&minOccupancy=86&maxOccupancy=120&page=2&activeSizeFilter=SEATS&groupByBuilding=false) so we can have a good guess on office availability as well as what renting prices currently look like.

Given the criteria of being in an office to accomodate c. 87 people, seems two options are available with one of them being slightly cheaper, which is the one we should explore renting, based in West 22nd street - 8th floor.

Annoyingly, there are no pictures to display yet for this ad:

![](Figures/screenshot29.png)

## Conclusions

1) After all the analysis, the top 3 cities seem to be good locations for our office, however in New York the breath of offering as well as the easier connection with airports are really strong reasons to choose it.

2) Despite the other criteria not being covered as part of the main analysis, the fact that we would be based in Midtown-Midtown South Manhattan means there are a lot of things nearby, so the chances most of the other criteria can also be met are high.

## Key documents/deliverables

a) Main_code.ipypnb

b) Foursquare_APIs.ipypnb

c) NYC_Web_Scraping.ipynb

d) My_functions.ipynb

e) Datasets folder:

    1) nyc_venues.csv
    2) nyc_venues_with_distances.csv
    3) sf_venues.csv
    4) sf_venues_with_distances.csv
    5) sj_venues.csv
    6) sj_venues_with_distances.csv
    7) nyc_real_state_only_price_info.csv
    8) nyc_real_state_webscraping.csv
    9) nyc_real_state_with_all_info.csv

f) Maps:

    1) nyc_map.html
    2) nyc_map_with_venues.html
    3) sf_map.html
    4) sf_map_with_venues.html
    5) sj_map.html
    6) sj_map_with_venues.html

g) src folder:

    1) main_code.py
    2) 4square-api.py
    3) web-scraping.py


![](Figures/nyc_image.jpg)

