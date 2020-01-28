# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:35:46 2019

@author: VIKKU
"""
import pandas as pd  
import folium as f
from folium import plugins
#from folium import Map,features,PolyLine
m=f.Map()
d=pd.read_csv("GoBackModi_12042018_India.csv")
#data=pd.read_csv("ikea.csv", dtype={"latitude": float})
#data2=pd.read_csv("ikea.csv", dtype={"longitude": float})
#d.head()
#row=list(d)

           
#test = f.Html(key, script=True)
loc=[]
#popup = f.Popup(test, max_width=2650)
d.dropna(axis=0,inplace=True)

z=len(d)
y=int(z)
for i in range(0,y):
    loc.append((d.iloc[i]['latitude'],d.iloc[i]['longitude']))

plugins.MarkerCluster(loc).add_to(m)
c=f.PolyLine(locations=[loc])
c.add_to(m)
m.save("xyz12.html")