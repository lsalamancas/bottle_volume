import cv2 as cv
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import matplotlib
import scipy.integrate as spi

class ImageArea:
    def __init__(self, image_path):
        #this class calculates the area of a boottle based on integration methods

        self.image_path = image_path
        self.image = cv.imread(image_path)
        if self.image is None:
            raise ValueError(f"Image at {image_path} could not be loaded.")
        self.height, self.width = self.image.shape[:2]
        

    def process_image(self):
        # Convert to grayscale
        gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)   
        # Apply Gaussian blur
        blurred = cv.GaussianBlur(gray, (5, 5), 0)  
        # Apply binary thresholding
        _, thresh = cv.threshold(blurred, 127, 255, cv.THRESH_BINARY_INV)
        # Find contours
        contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # plot contours and image
        cv.drawContours(self.image, contours, -1, (0, 255, 0), 3)
        plt.imshow(self.image)
        plt.axis('off')
        plt.show()
        # Calculate area using integration methods
        self.area = 0
        
    def get_area(self):
        return self.area