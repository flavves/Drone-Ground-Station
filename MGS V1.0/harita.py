# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:07:28 2022

@author: okmen
"""
"""
from gmplot import gmplot

# Initialize the map at a given point
gmap = gmplot.GoogleMapPlotter(39.8070302, 32.3905487, 744.57)

# Add a marker
gmap.marker(39.8070302, 32.3905487, 'cornflowerblue')

# Draw map into HTML file
gmap.draw("my_map.html")
"""

#çalışan bir yöntem fakat kurtarmaz :(
"""
GOOGLE_API_KEY="AIzaSyB5J2ljDu2KJ3bcbW9EyGjk5umtBLI_A0Y"


import os 
api_key = "AIzaSyB5J2ljDu2KJ3bcbW9EyGjk5umtBLI_A0Y"


from bokeh.io import output_notebook
output_notebook()
bokeh_width, bokeh_height = 500,400


from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.io import export_png

lat=39.8070302
lon=32.3905487
alt=0.083

def plot(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng, 
                               map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='Pays de Gex', 
             width=bokeh_width, height=bokeh_height)
    # beware, longitude is on the x axis ;-)
    center = p.circle([lng], [lat], size=10, alpha=0.5, color='red')
    show(p)
    return p

p = plot(lat, lon, map_type='satellite', zoom=17)
export_png(p, filename="plot.png")


"""
# Import necessary packages
import os 
import io
import folium
from folium import plugins
#import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
from streamlit_folium import st_folium
import streamlit as st
#Import data from EarthPy
#data = et.data.get_data('colorado-flood')


lat=39.8070302
lon=32.3905487

m = folium.Map(location=[lat, lon],zoom_start = 17)

#point olusturma
folium.Marker(
    location=[lat, lon], 
    popup='Drone', 
    icon=folium.Icon()
).add_to(m)
st_data=st_folium(m,width=725)




m.save(outfile= "test.html")
data=io.BytesIO()

roundnum = "function(num) {return L.Util.formatNum(num, 5);};"
plugins.MousePosition(position='topright', separator=' | ', prefix="Position:",lat_formatter=roundnum, lng_formatter=roundnum).add_to(m)
m










