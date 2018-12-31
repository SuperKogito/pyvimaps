# python3
"""
Created on Sun Dec 30 17:36:25 2018
@author: kogito
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import rgb2hex, Normalize
from Country import Country
### PARAMETERS FOR MATPLOTLIB :
import matplotlib as mpl
mpl.rcParams['font.size'] = 10.
mpl.rcParams['font.family'] = 'Comic Sans MS'
mpl.rcParams['axes.labelsize'] = 8.
mpl.rcParams['xtick.labelsize'] = 6.
mpl.rcParams['ytick.labelsize'] = 6.


plt.style.use('seaborn')
Germany = Country('DE')
fig, ax = plt.subplots()
m       = Basemap(llcrnrlon  = Germany.lower_longitude_bound-2,
                  llcrnrlat  = Germany.lower_lattitude_bound-2,
                  urcrnrlon  = Germany.upper_longitude_bound+2,
                  urcrnrlat  = Germany.upper_lattitude_bound+1,
                  resolution = 'i',
                  projection = 'merc',
                  lat_0      = 34,
                  lon_0      = 10)

shp_info     = m.readshapefile('shapefiles/DE/DE', 'states')
states       = sorted(Germany.states)
# population_desities_data: Inhabitants per sq. mi.(1998, 2006)
# source: http://www.toponline.org/books/kits/germany%20today/GTpdf/Handout3.pdf
population_desities_data = {
                            'Berlin'                       : {1998: 9941, 2006: 9888},
                            'Hamburg'                      : {1998: 5822, 2006: 5939},
                            'Bremen'                       : {1998: 4295, 2006: 4032}, 
                            'Nordrhein-Westfalen'          : {1998: 1465, 2006: 1370},
                            'Saarland'                     : {1998: 1079, 2006: 1052},
                            'Baden-Württemberg'            : {1998: 755,   2006: 778},
                            'Hessen'                       : {1998: 740,   2006: 745},
                            'Sachsen'                      : {1998: 634,   2006: 598},
                            'Rheinland-Pfalz'              : {1998: 525,   2006: 529},
                            'Schleswig-Holstein'           : {1998: 454,   2006: 465},
                            'Bayern'                       : {1998: 444,   2006: 459},
                            'Niedersachsen'                : {1998: 430,   2006: 435},
                            'Thüringen'                    : {1998: 392,   2006: 371},
                            'Sachsen-Anhalt'               : {1998: 338,   2006: 309},
                            'Brandenburg'                  : {1998: 231,   2006: 224},
                            'Mecklenburg-Vorpommern'       : {1998: 196,   2006: 189}
                          }
                           
                           
                           
values       = [population_desities_data[key][1998] for key in sorted(population_desities_data.keys())]
popdensity   = dict(zip(states, values))
nodata_color = "white"
colors       = {}
statenames   = []
patches      = []

cmap = plt.cm.viridis
vmin = min(popdensity.values())
vmax = max(popdensity.values())
norm = Normalize(vmin=vmin, vmax=vmax)
# color mapper to covert values to colors
mapper = ScalarMappable(norm=norm, cmap=cmap)

for shapedict in m.states_info:
    statename = shapedict['NAME_1']
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
cax = fig.add_axes([0.37, 0.2, 0.3, 0.01]) # posititon
cb  = ColorbarBase(cax, cmap=cmap, norm = norm, orientation = 'horizontal')
plt.show()
