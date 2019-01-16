# python
"""
Created on Sun Jan 13 22:22:18 2019
@author: kogito
"""
 

""" This is a small usage demo """
from random import randint
from pyvimaps.Tunisia import Tunisia
from pyvimaps.Germany import Germany

# Define data
data    = [i for i in range(24)]

## Tunisia plot
Tunisia = Tunisia()
Tunisia.plot_data(data, 'Random densities', 'Blues')
#Tunisia.print_data_dict()
print(Tunisia.data_dict)

# Germany plot
Germany = Germany()
Germany.plot_data(data, 'Random densities', 'Blues')
#Germany.print_data_dict()
print(Germany.data_dict)