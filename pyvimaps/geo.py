import shapefile
import numpy as np
import pandas as pd
import matplotlib.cm
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.colors import Normalize
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PatchCollection

from numpy import arange
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
import geopandas as gpd
import fiona
from random import randint

plt.style.use('seaborn')

def generate_colors(values_list):
    N = len(values_list)

    # red-green colormap:
    cdict = {'red':   [(0.0, 1.0, 1.0),  # red decreases
                       (1.0, 0.0, 0.0)],

             'green': [(0.0, 0.0, 0.0),  # green increases
                       (1.0, 1.0, 1.0)],

             'blue':  [(0.0, 0.0, 0.0),  # no blue at all
                       (1.0, 0.0, 0.0)] }

    red_green_cm = LinearSegmentedColormap('RedGreen', cdict, N)
    colors       = cm.get_cmap(red_green_cm, N)
    clr          = [colors(i) for i in range(colors.N, -1, -1)]
    return red_green_cm, clr

def read_file(filename, bbox=None, **kwargs):
    path_or_bytes = filename
    reader        = fiona.open

    with reader(path_or_bytes, **kwargs) as features:
        crs    = features.crs
        f_filt = features

        columns = list(features.meta["schema"]["properties"]) + ["geometry"]
        gdf = gpd.GeoDataFrame.from_features(f_filt, crs=crs, columns=columns)

        header = ['id_0',
                  'iso',
                  'name',
                  'id',
                  'state_name',
                  'type_1',
                  'engtype_1',
                  'nl_name',
                  'varname',
                  'geometry']

        gdf.columns = header
        df = gdf[['id','iso', 'name', 'state_name', 'geometry']]
    return df



fig, ax = plt.subplots(figsize=(10,10))
df      = read_file("shapefiles/TN/TN.shp")
df      = df.assign(values=pd.Series( [randint(10, 100) for i in range(24)] ))
df      = df.sort_values('values')

data    = [int(i) for i in df['values'].values]
red_green_cm, colors = generate_colors(data)
df      = df.assign(colors=pd.Series( colors ))

for i in range(24):
    poly = df['geometry'][i]
    ax.add_patch(PolygonPatch(poly, fc=colors[i], ec='black'))
    ax.axis('scaled')

# adding colorbar:
ax_cb = fig.add_axes([0.75, 0.3, 0.03, 0.5])
norm  = mpl.colors.Normalize(vmin=data[0], vmax=data[-1])
cb    = mpl.colorbar.ColorbarBase(ax_cb, cmap=red_green_cm, norm=norm, orientation='vertical')
plt.show()

print(df['state_name'].head)
