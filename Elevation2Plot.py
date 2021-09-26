import requests
import sys
import json
import pandas as pd
from geopy import distance
from zipfile import ZipFile
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

distances=[0,]
elevations=[]
coorListFull =[]

def parse_kmz():
    """Extract and read coordinates from KML file"""
    try:
        file = sys.argv[1]
    except IndexError:
        raise SystemExit(f"====\nUsage: {sys.argv[0]} <.kmz file name>\n====")
    with ZipFile(file, 'r') as kmz:
        with kmz.open('doc.kml', 'r') as kml:
            print("File  successfully loaded...")
            bs_data = bs(kml, 'lxml')
            print("Listing coordinates...")
            tagData = bs_data.find('coordinates').text.strip().split(' ')
            print("Requesting elevation data...\nThis might take a moment...")
            get_elevation(tagData)
            print("Calculating distances...")
            get_distance(coorListFull)

def get_elevation(coorList):
    """
    Perform GET request to the server [https://api.open-elevation.com]
    More info: https://open-elevation.com
    """
    for item in coorList:
        query = item.split(',')[1] + ',' + item.split(',')[0]
        coorListFull.append(query)
        uri = f'https://api.open-elevation.com/api/v1/lookup?locations={query}'
        #print(f'Trying ID >> {query}')
        response = requests.get(uri)
        data = response.json()
        if data['results'] != None:
            elevations.append(data['results'][0]['elevation'])

def get_distance(coorList):
    """Calculate the distance between coordinates"""
    a = 1
    while a < len(coorList):
        distances.append(distance.distance(coorList[0], coorList[a]).m)
        a += 1
    plot(distances, elevations)

def plot(dist, elev):
    """Generate the plot"""
    X_Y_Spline = make_interp_spline(dist, elev)
    X_ = np.linspace(min(distances), max(distances), 30)
    Y_ = X_Y_Spline(X_)
    f = plt.figure()
    f.set_figheight(1)
    plt.plot(X_, Y_) #Smoother plot [rather than >> plt.plot(distances, elevations)]

    plt.title("Elevation Data")
    plt.xlabel("Distance (m)")
    plt.ylabel("Elevation (m)")
    print("Plot successfully generated...")
    plt.show()
    print('Done')

if __name__ == '__main__':
    parse_kmz()
