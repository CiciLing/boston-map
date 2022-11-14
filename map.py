import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, HTML


m = folium.Map(location=[42.3601,-71.0942],zoom_start=14, width="80%")
data = pd.read_csv('placelist.csv')
place_name = data['Place'].tolist()
longtitude = data['Longitude'].tolist()
latitude = data['Latitude'].tolist()
category = data['Type'].tolist()

for i in range(len(place_name)):
    if category[i] == 'Historical spots':
        folium.Marker(location=[latitude[i],longtitude[i]],popup=place_name[i], tooltip=place_name[i], icon=folium.Icon(color='black')).add_to(m)
    else:
        folium.Marker(location=[latitude[i], longtitude[i]], popup=place_name[i], tooltip=place_name[i], icon=folium.Icon(color='black',icon_color='#FFFF00')).add_to(m)

