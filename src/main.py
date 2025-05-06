import os
import sys
import numpy as np  
import matplotlib.pyplot as plt
from image_area_calculation import BottleVolume

if __name__ == "__main__":
    resources_path = os.getcwd() + '/resources/'
    print(resources_path)
    Bottle = BottleVolume(os.path.join(resources_path, "cocacola2.jpg"))
    Bottle.process_image()
    print(Bottle.get_volume('simpson'))
    print(Bottle.get_volume('trapezoid'))
    print(Bottle.get_volume('rectangle'))


