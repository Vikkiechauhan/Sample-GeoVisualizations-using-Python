import numpy as np
import pandas as pd
import holoviews as hv
import geoviews as gv
import geoviews.tile_sources as gts
from cartopy import crs as ccrs
from geoviews import opts
import os

from bokeh.tile_providers import STAMEN_TONER
from bokeh.models import WMTSTileSource
hv.notebook_extension('bokeh')

tiles = {'OpenMap': WMTSTileSource(url='http://c.tile.openstreetmap.org/{Z}/{X}/{Y}.png'),
         'ESRI': WMTSTileSource(url='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{Z}/{Y}/{X}.jpg'),
         'Wikipedia': WMTSTileSource(url='https://maps.wikimedia.org/osm-intl/{Z}/{X}/{Y}@2x.png'),
         'Stamen Toner': STAMEN_TONER}
#d=pd.read_csv("GoBackModi_12042018_India.csv",encoding="ISO-8859-1")
#hv.NdLayout({name: gv.WMTS(wmts, extents=(0, -90, 360, 90), crs=ccrs.PlateCarree())
 #           for name, wmts in tiles.items()}, kdims=['Source']).cols(2)
#lat=[],lon=[],usersc=[],usernm=[],times=[]
#popup = f.Popup(test, max_width=2650)
#d.dropna(subset=['latitude','longitude'], inplace=True)

#d.dropna(subset=['tweetCreated'],inplace=True)

#for i in range(0,len(d)):
my={}
d = pd.read_csv("GoBackModi_12042018_India.csv", encoding="ISO-8859-1")
d.dropna(subset=['latitude','longitude'], inplace=True)

#for i  in range(0,len(d)):
  #  z1=d.iloc[i]['latitude']
  #  z2=d.iloc[i]['longitude']
     
 #   nyclat = (float(z1), float(z2))
#    nyctim= ( d.iloc[i]['tweetCreated'])

#popu = gv.Points([nyclat,nyctim])
    
popu=gv.Dataset(d, kdims=['tweetCreated'])
pop1=(gv.WMTS(tiles['Wikipedia']) *\
popu.to(gv.Points, kdims=['latitude', 'longitude'],
              vdims=['tweetCreated'],width=500, height=475, size=12, color='black' ,crs=ccrs.PlateCarree()))
hv.renderer('bokeh').save(pop1, 'graph8', fig='png',holomap='gif')
    



#renderer=hv.renderer('bokeh')
#ab=renderer.save(pop1, 'graph6', fmt='png')

#with imageio.get_writer('internship.gif', mode='I') as writer:
#    for filena in ab:
 #       image = imageio.imread(filena)
  #      writer.append_data(image)
# Convert to bokeh figure then save using bokeh
#plot = renderer.get_plot(pop1).state
