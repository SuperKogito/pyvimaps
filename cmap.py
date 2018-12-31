import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import rgb2hex, Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.patches import Polygon
from matplotlib.colorbar import ColorbarBase

m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
ax  = plt.gca() 
fig = plt.gcf()
shp_info = m.readshapefile('uss/cb_2017_us_state_5m','states',drawbounds=True)

popdensity = {'ALABAMA': 37,
             'ALASKA': 1,
             'ARIZONA': 161,
             'ARKANSAS': 35,
             'CALIFORNIA': 1854,
             'COLORADO': 104,
             'CONNECTICUT': 170,
             'DELAWARE': 53,
             'DISTRICT OF COLUMBIA': 83,
             'FLORIDA': 364,
             'GEORGIA': 350,
             'HAWAII': 15,
             'IDAHO': 16,
             'ILLINOIS': 553,
             'INDIANA': 109,
             'IOWA': 60,
             'KANSAS': 47,
             'KENTUCKY': 50,
             'LOUISIANA': 48,
             'MAINE': 17,
             'MARYLAND': 187,
             'MASSACHUSETTS': 351,
             'MICHIGAN': 260,
             'MINNESOTA': 170,
             'MISSISSIPPI': 16,
             'MISSOURI': 119,
             'NA': 11,
             'NEBRASKA': 28,
             'NEVADA': 21,
             'NEW HAMPSHIRE': 32,
             'NEW JERSEY': 676,
             'NEW MEXICO': 20,
             'NEW YORK': 993,
             'NORTH CAROLINA': 266,
             'NORTH DAKOTA': 5,
             'OHIO': 271}

nodata_color = "darkorange"
colors={}
statenames=[]
patches = []

cmap = plt.cm.summer
vmin = min(popdensity.values()); vmax = max(popdensity.values())
norm = Normalize(vmin=vmin, vmax=vmax)
# color mapper to covert values to colors
mapper = ScalarMappable(norm=norm, cmap=cmap)

for shapedict in m.states_info:
    statename = shapedict['NAME'].upper()
    if statename in popdensity:
        pop = popdensity[statename]
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
# plt.title('Filling State Polygons by Population Density')

# put legend for no data states
#if p_no is not None:
    #plt.legend((p_no,), ('No data',))

# construct custom colorbar
cax = fig.add_axes([0.27, 0.1, 0.5, 0.05]) # posititon
cb = ColorbarBase(cax,cmap=cmap,norm=norm, orientation='horizontal')
#cb.ax.set_xlabel('Population density of U.S.A.')
plt.show()