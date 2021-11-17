from argparse import ArgumentParser
from haversine import haversine
from vincenty import vincenty
import sys

class Zipcode:
    """Ask the user to input a zipcode and return a list of vaccine clinics in latitude and longitude
    
    Attributes: zipcodes (str)
    
    Returns: appended dictionary of longitudes and latitudes (floats)"""
    def __init__(self, filepath):
        self.zipcodes = [ ]
        with open(filepath, "r", encoding="utf-8") as f:
            for i in f: 
                zipdict = { }
                place, zip, lat, lon= i.split("\t")
                zipdict["place"] = str(place)
                zipdict["zip"] = int(zip)
                zipdict["lat"] = float(lat)
                zipdict["lon"] = float(lon)
                self.zipcodes.append(zipdict)
                
    def near(self, lat, lon, n = 5):
        multi_zip = [i for i in self.zipcodes if i["zip"]
        loc1 = (lat,lon)
        multi_zip = sorted(multi_zip, key = lambda entry:get_dist(loc1,(entry["lat"], entry["lon"])))
        return multi_zip[:n]
    
    def get_dist(p1, p2, miles=False):
    """Calculate the distance between two latitude/longitude coordinates.
    
    Args:
        p1 float: latitude and longitude of one location.
        p2 float: latitude and longitude of second location.
        miles (bool): if True, return result in terms of miles
    
    Returns:
        float: the distance between p1 and p2
    """
    dist = vincenty(p1, p2, miles=miles)
    if not dist:
        dist = haversine(p1, p2, unit='mi' if miles else 'km')
    return dist

def main(filepath, lat, lon):
    """ ask for an input of a zipcode and return the zipcode inputted

    Args:
        filepath(str): txt file with strings
        lat(float)
        lon(float)
    
    Returns:
        zipcode(int)
    """
    print("Please input a zipcode:")
    a = input()
        return a

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("filepath", help = "path to a file with strings")
    parser.add_argument("lat", help = "float closest to provided zipcode location")
    parser.add_argument("lon", help = "float closest to provided zipcode location")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(filepath, lat, lon)