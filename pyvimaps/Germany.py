# python
"""
@date  : 30.12.2018
@author: SuperKogito
"""
from pyvimaps.Country import Country
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import rgb2hex, Normalize

class Germany():
    """
        Class Germany to handle the germany shapes file, format and plot the
        data as a geo stats plot.
    """

    def __init__(self):
        self.germany      = Country('DE')
        self.fig, self.ax = plt.subplots()
        self.tn_map       = Basemap(llcrnrlon  = self.germany.lower_longitude_bound-0.25,
                                    llcrnrlat  = self.germany.lower_lattitude_bound-1,
                                    urcrnrlon  = self.germany.upper_longitude_bound+3,
                                    urcrnrlat  = self.germany.upper_lattitude_bound+0.25,
                                    resolution = 'i',
                                    projection = 'merc',
                                    lat_0      = 34,
                                    lon_0      = 10)

        self.sahpe_info = self.tn_map.readshapefile('pyvimaps/shapefiles/DE/DE', 'states')
        self.states     = list(set([shape_dict['NAME_1'] for shape_dict in self.tn_map.states_info]))

    def construct_data_dict(self, states, data):
        zipped    = zip(self.states, data)
        data_dict = {key: value for (key, value) in zipped}
        return data_dict

    def print_data_dict(self):
        print('--------------------------------')
        for key, value in self.data_dict.items():
            print("%25s : %d" % (key, value))
        print('--------------------------------')

    def plot_data(self, data, title, cmap_name):
        """
            Plot data as a states map.
        """
        self.data_dict = self.construct_data_dict(self.states, data)
        nodata_color   = "white"
        colors         = {}
        state_names    = []
        no_data_poly   = None

        # prepare color nuances
        cmap = plt.get_cmap(cmap_name)
        vmin = min(self.data_dict .values())
        vmax = max(self.data_dict .values())
        norm = Normalize(vmin=vmin, vmax=vmax)

        # color mapper to covert values to colors
        mapper = ScalarMappable(norm=norm, cmap=cmap)

        for shape_dict in self.tn_map.states_info:
            state_name = shape_dict['NAME_1']
            if state_name in self.data_dict :
                pop               = self.data_dict [state_name]
                colors[state_name] = mapper.to_rgba(pop)
                state_names.append(state_name)
            else:
                state_names.append(state_name)
                colors[state_name] = nodata_color

        for nshape, seg in enumerate(self.tn_map.states):
            color = rgb2hex(colors[state_names[nshape]])
            poly  = Polygon(seg, facecolor = color, edgecolor=color)
            if (colors[state_names[nshape]] == nodata_color):
                no_data_poly = poly
            self.ax.add_patch(poly)
        plt.title(title)

        # put legend for no data states
        if no_data_poly is not None: plt.legend((no_data_poly,), ('No data',))

        # construct custom colorbar
        colorbar_axis = self.fig.add_axes([0.67, 0.25, 0.01, 0.5]) # posititon
        colorbar  = ColorbarBase(colorbar_axis, cmap=cmap, norm = norm, orientation = 'vertical')
        plt.show()
