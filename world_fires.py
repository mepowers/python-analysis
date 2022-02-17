"""
Plot all wildfires (brightness and Fire Radiative Pixel (FRP)) 
from a given day onto a world map

@author: mepowers
"""

#import packages
import pandas as pd
from plotly.graph_objs import Layout
from plotly import offline

# Read fires data into a dataframe
fires = pd.read_csv("data/world_fires_1_day.csv")
# Normalize Brightness to use as a colorscale.  Otherwise all colors look the same.
bright = fires['brightness'] - fires['brightness'].min()

# Create graph object
data = [{
    'type': 'scattergeo',
    'lon': fires['longitude'],
    'lat': fires['latitude'],
    'marker': {
        # Marker size = FRP, or Fire Radiative Pixel
        'size': [f/100 for f in fires['frp']],
        # Marker color = brightness of fire
        'color': bright,
        # Brights fires are red; least bright are blue
        'colorscale': 'Portland',
        'colorbar': {'title': 'Brightness'}
    }    
}]

# Set title of plot
my_layout = Layout(title='World Fires as of ' + fires['acq_date'].min())

# Plot map to html
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')