""" Download data set and then geocode all the addresses. """

import re
import StringIO
import zipfile

import requests
import pandas as pd
from geopy.geocoders import Nominatim


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
    replace = " Metro Area| Micro Area| CSA"
    fgeodata = geodata.apply((lambda mystr: re.sub(replace, "", mystr)))

    return fgeodata

def handle_output(response):
    """ Parse http response from Nominatim. """
    pass

def reverse_geocode(fgeodata):
    """ Perform geocoding on the data using Nominatim. """
    geolocator = Nominatim()
    location = geolocator.geocode
    
    

    
        
    
