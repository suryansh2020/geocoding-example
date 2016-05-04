""" Download data set and then geocode all the addresses. 

Note that Nominatim will start rate limiting you after a few 
thousand requests.

"""

import io
import re
import StringIO
import zipfile
import logging
from logging.config import fileConfig

import requests
import pandas as pd
from geopy.geocoders import Nominatim


logging.basicConfig(filename=  "geocoding.log",
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')
link = "https://s3.amazonaws.com/packrat-bundles/SBO_2012_00CSA01.zip"

def read_file(link, table='SBO_2012_00CSA01_with_ann.csv'):
    """ Unzip table and return pd.DataFrame. """
    response = requests.get(link)

    if response.status_code != requests.codes.ok:
        raise Exception("Retry the download :-( ")

    z = zipfile.ZipFile(io.BytesIO(response.content))
    with z.open(table) as myzip:
        csvstr = myzip.read()

    df = pd.read_csv(StringIO.StringIO(csvstr), dtype=object)
    return df

def format_data(df, geocol='GEO.display-label'):
    """ Format the csv file so it's ready for geocoding. """
    geodata = pd.Series(df[geocol].unique())

    # regional names
    replace = " Metro Area| Micro Area| CSA"
    fgeodata = geodata.apply((lambda mystr: re.sub(replace, "", mystr)))

    # match to actual cities
    replace = "\-.*(?=,)"
    fgeodata = fgeodata.apply((lambda mystr: re.sub(replace, "", mystr)))

    # manage data frame
    geodata_ref = pd.concat([fgeodata, geodata], axis=1)
    geodata_ref = geodata_ref[1:]
    geodata_ref.columns = ['fgeodata', 'geodata']
    
    return geodata_ref

def geocode(address):
    """ Perform geocoding on the data using Nominatim. """
    geolocator = Nominatim()
    
    try:
        location = geolocator.geocode(str(address))
        coordinates = (location.longitude, location.latitude)
        logging.info('found address: {}'.format(str(address)))
        return coordinates

    except:
        logging.error("unable to find address: {}".format(address))
        return ("", "")

def update_data(geodata_ref):
    geodata_ref['longitude'] = ''
    geodata_ref['latitude'] = ''

    for index, row in geodata_ref.iterrows():

        try:
            longitude, latitude = geocode(row['fgeodata'])

            geodata_ref.iloc[index]['longitude'] = longitude
            geodata_ref.iloc[index]['latitude'] = latitude

        except IndexError: #TODO: resolve index error
            pass

    return geodata_ref

def geocoded_data(geodata_ref, df):
    """ Join geocoded data to original data frame. """
    result = pd.merge(left=df, right=geodata_ref,
                      on=['GEO.display-label', 'geodata'])
    #TODO: KeyError: might be an issue with unicode
    return result




        
    
    

    
        
    
