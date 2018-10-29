
"""""
Germany address Anonymiser (germany_anon.py)
This script converts full addresses to anonymised latitude and longitude coordinates using 2 geocoders.
The fll address is first searched for using geocoder's google geolocator, if it is not found it is searched
for a second time using geopy's Nominatim geoooder. The longitude and latitude returned by the geocoders
are then anonymised by rounding the longitude and latitude to 2 decimal places.

If the geocoders are not able to find the post code then NaNs will be stored for longitude and latitude.

The output is saved to ***_anon.csv.

changelog:
    26 Oct 2018 by Zuo Zhang
        1. A parameter GOOGLE_API_KEY is added to use google geocoder properly, if not no geo info will be 
            returned from google
        2. Add a pause time (0.05s) for google geo server enquiry and 1.05s for Nominatim (open street map)
            due to server limitations. Flood searches may cause blocking.Google allows 30 searches per second
            and Nominatim allows 1 per second.
        3. Add fileEncoding parameter to specify the encoding of the input csv file (text file in nature). 
            Common encodings include 'utf-8', 'cp1252' (for ANSI encodig), 'gb2312' (for Chinese). File will 
            not be able to load if wrong encoding info is provided.
            
    

"""

import pandas as pd
import geocoder
import geopy
from geopy.geocoders import Nominatim
import numpy as np
import time

def anony(file, fileEncoding, country, google_api_key):


    
    # all participants and addresses saved in dataframe
    addresses = pd.read_csv(file,encoding= fileEncoding, names=['ID','address']).drop(0).dropna()
    n = len(addresses)
    
    # new dataframe and lists to store lats and lons created
    latlon = pd.DataFrame()
    latlon['ID'] = addresses['ID']
    lats = []
    lons = []
    
    # for loop to convert each address to lat lon
    for i in range(1, n+1):
        
        print (i)
        # get a address
        address = addresses['address'][i]
    
        # try to find address with first geolocator
        g = geocoder.google(('%s, %s')% (address, country),key=google_api_key)
        time.sleep(0.05)
        ltln = g.latlng
    
        # if address not found try a second geolocator
        if ltln is None:
            g2 = Nominatim(user_agent="IMAGEN").geocode(('%s, Germany')%address)
            time.sleep(1.05)
            # if address still not found store NaNs
            if g2 is None:
                lats.append(np.nan)
                lons.append(np.nan)
    
            # store information from second geocoder
            else:
                lat2 = round(g2.latitude, 2)
                lats.append(lat2)
                lon2 = round(g2.longitude, 2)
                lons.append(lon2)
    
        # store info from first geocoder
        else:
            lat = round(ltln[0], 2)
            lats.append(lat)
            lon = round(ltln[1], 2)
            lons.append(lon)
    
    # store all info together lat long in dataframe
    latlon['lat'] = lats
    latlon['lon'] = lons
    missing = latlon['lat'].isnull().sum()
    print('There are %d address(s) that cannot be found.' %missing)
    
    # convert dataframe to .csv for external storage
    new_file = file[:-4] + '_anon.csv'
    latlon.to_csv(new_file)
    print('Please find the anonymised addresses in the file named %s' % new_file)
    
    # return dataframe
    return(latlon)
