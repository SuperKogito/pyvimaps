# python
"""
Created on Sun Jan 13 22:22:18 2019
@author: kogito
"""
 

""" This is a small usage demo """
from pyvimaps.Tunisia import Tunisia
from random import randint

Tunisia = Tunisia()
data    = [i for i in range(22)]

Tunisia.plot_data(data, 'State population density', 'Blues')
Tunisia.print_data_dict()
print(Tunisia.data_dict)
