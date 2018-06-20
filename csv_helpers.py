import pandas
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut
import time

def return_new_csv(file):
    def capitalOrLowercase(data):
        for values in data.columns.values:
            if values == "Address":
                return "Address"
            elif values == "address":
                return "address"

    def geocode(address):
        try:
            return nom.geocode(address)
        except GeocoderTimedOut:
            return nom.geocode(address)

    data = pandas.read_csv(file)
    nom = Nominatim()
    lat = []
    lon = []
    aOrA = capitalOrLowercase(data)

    for address in data[aOrA]:
        coordinates = geocode(address)
        try:
            lat.append(coordinates.latitude)
            lon.append(coordinates.longitude)
        except:
            lat.append(None)
            lon.append(None)
        time.sleep(.5)

    data["Latitude"] = lat
    data["Longitude"] = lon
    data.to_csv("geo_"+file[5:])
    html_file = "geo_" + file[5:]
    html_file = html_file[:-4] + ".html"
    path = r'C:\Users\andy\Desktop\geocoder\templates\\'
    data.to_html(path+html_file, classes=["table","table-dark"])

    

def contains_address(file):
    data = pandas.read_csv(file)
    for values in data.columns.values:
        if values == "Address" or values == "address":
            return True
    return False

