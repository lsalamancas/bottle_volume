import cv2 as cv
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from scipy.integrate import simpson


class BottleVolume:
    def __init__(self, image_path):
        #this class calculates the area of a boottle based on integration methods

        self.image_path = image_path
        self.image = cv.imread(image_path)
        self.bottle_heigh = 23 #cm 
        if self.image is None:
            raise ValueError(f"Image at {image_path} could not be loaded.")
        self.height, self.width = self.image.shape[:2]
        

    def process_image(self):
        # Convert to grayscale
        gray = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        cv.imwrite("resources/bottle_gray.jpg", gray)   
        # Apply Gaussian blur
        blurred = cv.GaussianBlur(gray, (5, 5), 0)  
        cv.imwrite("resources/bottle_blurred.jpg", blurred)   
        # Apply binary thresholding
        _, thresh = cv.threshold(blurred, 175, 255, cv.THRESH_BINARY_INV)
        cv.imwrite("resources/bottle_thresh.jpg", thresh)  
        # Find contours
        contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # plot contours and image
        cv.drawContours(self.image, contours, -1, (0, 255, 0), 3)
        #create a blank image 
        contour_image = np.ones_like(self.image) * 255
        cv.imwrite("resources/bottle_withcontour.jpg", self.image)  

        # Draw the countour over the blank image
        cv.drawContours(contour_image, contours, -1, (0, 0, 0), 5)
        cv.imwrite("resources/bottle_contour.jpg", contour_image)

        #height and with to normalize the image

        h, w = self.image.shape[:2]

        medium_bottle = contour_image[:,w//2:] 
        # Calculate area using integration methods
        img_rotated = cv.rotate(medium_bottle, cv.ROTATE_90_COUNTERCLOCKWISE)
        plt.imshow(img_rotated)
        plt.axis('off')
        plt.savefig('resources/countour_rotated.png')
        
        if len(img_rotated.shape) == 3:  # Check if it has multiple channels
            img_rotated = cv.cvtColor(img_rotated, cv.COLOR_BGR2GRAY)

        cv.imwrite("resources/imagen_guardada.jpg", thresh)
        
        scale_to_mm = self.bottle_heigh / h

        black_points = np.column_stack(np.where(img_rotated < 1))
        self.function_cm = scale_to_mm*black_points[:,0:2]
        self.function_cm = self.function_cm[(self.function_cm[:, 0] >= 5.2) & ((self.function_cm[:, 1] <= 21.5))]
        plt.scatter(self.function_cm[:,1], self.function_cm[:,0], color='red', s=2)
        plt.title("Contour in cm")
        plt.ylabel('cm')
        plt.xlabel('cm')
        plt.gca().invert_yaxis()  # Invert Y to match image coordinates
        plt.savefig('functionplot.png')


    def get_volume(self, method):
        if method == 'simpson':
            return  np.pi * simpson(self.function_cm[:,1]**2, self.function_cm[:,0])
        if method == 'trapezoid':
            return np.pi * np.trapz(self.function_cm[:,1]**2, self.function_cm[:,0])
        if method == 'rectangle':
            dx = np.diff(self.function_cm[:,0])  # Step size between height points
            rect_areas = np.pi * (self.function_cm[:,1]**2) * dx  # Area of each rectangle slice
            return np.sum(rect_areas) 
