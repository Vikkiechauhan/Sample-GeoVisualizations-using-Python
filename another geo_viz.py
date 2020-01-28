# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:52:50 2019

@author: VIKKU
"""

import pandas as pd  
import folium as f
from folium import plugins
from folium.plugins import TimestampedGeoJson
#from folium import Map,features,PolyLine
#m=f.Map()
d=pd.read_csv("GoBackModi_12042018_India.csv")
#data=pd.read_csv("ikea.csv", dtype={"latitude": float})
#data2=pd.read_csv("ikea.csv", dtype={"longitude": float})
#d.head()
#row=list(d)
loc=[]
#popup = f.Popup(test, max_width=2650)
d.dropna(subset=['latitude','longitude'], inplace=True)
d['tweetCreated']=pd.to_datetime(d['tweetCreated'], errors='coerce')
d.dropna(subset=['tweetCreated'],inplace=True)

d.sort_values(by='tweetCreated', ascending=True)


def create_geojson_features(df):
    #print('> Creating GeoJSON features...')
    features = []
    for _, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type':'Point', 
                'coordinates':[d['longitude'],d['latitude']]
            },
            'properties': {
                'time': row['tweetCreated'].date().__str__(),
                #'style': {'color' : row['color']},
                #'icon': 'circle',
                #'iconstyle':{
                 #   'fillColor': row['color'],
                 #   'fillOpacity': 0.8,
                 #   'stroke': 'true',
                 #   'radius': 7
                #}
            }
        }
        features.append(feature)
    return features
def make_map(features):
    #print('> Making map...')
    m=f.Map()
    a={}
    z=0.3*len(d)
    y=int(z)
    for i in range(0,y):
        z1=d.iloc[i]['latitude']
        z2=d.iloc[i]['longitude']
        try:
            loc.append(( float(z1),float(z2)))
            #a={i:{d.iloc[i]['tweetCreated']:{loc}}}
        except:
            pass


    plugins.MarkerCluster(loc).add_to(m)

    TimestampedGeoJson(
        {'type': 'FeatureCollection',
        'features': features}
        , period='P1M'
        , add_last_point=True
        , auto_play=False
        , loop=False
        , max_speed=1
        , loop_button=True
        , date_options='YYYY/MM'
        , time_slider_drag_update=True
    ).add_to(m)
    #print('> Done.')
    return pollution_map
def plot_pollutant():
    #print('Mapping {} pollution in Belgium in 2013-2015'.format(pollutants[pollutant_ID]['name']))
    #df = load_data(pollutant_ID)
    #df = clean_data(df)
    #df = prepare_data(df, pollutant_ID)
    features = create_geojson_features(d)
    return make_map(features)
m=plot_pollutant()
m.save("abc140.html")