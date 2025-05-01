import os
import sys
import numpy as np  
import matplotlib.pyplot as plt
from image_area_calculation import ImageArea

if __name__ == "__main__":
    resources_path = os.getcwd() + '/resources/'
    print(resources_path)
    image_area = ImageArea(os.path.join(resources_path, "cocacola.png"))
    image_area.process_image()
    
