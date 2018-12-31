# python
"""
@date  : 30.12.2018
@author: SuperKogito
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import rgb2hex, Normalize
from Country import Country

Tunisia = Country('TN')

fig, ax = plt.subplots()
m       = Basemap(llcrnrlon  = Tunisia.lower_longitude_bound,
                  llcrnrlat  = Tunisia.lower_lattitude_bound,
                  urcrnrlon  = Tunisia.upper_longitude_bound,
                  urcrnrlat  = Tunisia.upper_lattitude_bound,
                  resolution = 'i',
                  projection = 'merc',
                  lat_0      = 34,
                  lon_0      = 10)


shp_info = m.readshapefile('shapefiles/TN', 'states')

popdensity0 = {'ARIANA':10,
              'BÉJA':50,
              'BEN AROUS (TUNIS SUD)':150,
              'BIZERTE':70,
              'GABÈS':20,
              'GAFSA':50,
              'JENDOUBA':200,
              'KAIROUAN':240,
              'KASSÉRINE':100,
              'KEBILI':210,
              'LE KEF':230,
              'MÉDENINE':0,
              'MAHDIA':700,
              'MANUBAH':110,
              'MONASTIR':211,
              'NABEUL':122,
              'SFAX':46,
              'SIDI BOU ZID':15,
              'SILIANA':90,
              'SOUSSE':74,
              'TATAOUINE':170,
              'TOZEUR':230,
              'TUNIS':300,
              'ZAGHOUAN': 271}
states = Tunisia.states
values = [10, 50,  150,  70,  20,  50,  200,  240,  100,  210,  230,  0,  700,
          110,  211,  122,  46,  15,  90,  74,  170,  230,  300,  271]
 
popdensity   = dict(zip(states, values))
nodata_color = "white"
colors       = {}
statenames   = []
patches      = []

cmap = plt.cm.Oranges
vmin = min(popdensity.values())
vmax = max(popdensity.values())
norm = Normalize(vmin=vmin, vmax=vmax)
# color mapper to covert values to colors
mapper = ScalarMappable(norm=norm, cmap=cmap)

for shapedict in m.states_info:
    statename = shapedict['NAME_1'].upper()
    if statename in popdensity:
        pop               = popdensity[statename]
        colors[statename] = mapper.to_rgba(pop)
        statenames.append(statename)
    else:
        statenames.append(statename)
        colors[statename] = nodata_color

for nshape,seg in enumerate(m.states):
    color = rgb2hex(colors[statenames[nshape]])
    poly = Polygon(seg,facecolor=color,edgecolor=color)
    if (colors[statenames[nshape]] == nodata_color):
        p_no = poly
    ax.add_patch(poly)
plt.title('Filling State Polygons by Population Density')

# put legend for no data states
#if p_no is not None: plt.legend((p_no,), ('No data',))

# construct custom colorbar
cax = fig.add_axes([0.65, 0.25, 0.01, 0.5]) # posititon
cb  = ColorbarBase(cax, cmap=cmap, norm = norm, orientation = 'vertical')
plt.show()
