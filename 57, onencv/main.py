import cv2
import sys 
import numpy as np

name_img = "forest_dark.png"

class OpenRead:
    def __init__(self, path, new_name):
        self.image = cv2.imread(cv2.samples.findFile(path))
        self.new_name = new_name

    def open_image(self):
        cv2.imshow('Display', self.image)
        k = cv2.waitKey(0)
        if k == ord('s'):
            self.save_image()
    
    def save_image(self):
        cv2.imwrite(self.new_name, self.image)
        

class Editor(OpenRead):
    def __init__(self, path, new_name):
        super().__init__(path, new_name)
    
    def contrast_brightness(self, alpha, beta):
        new_image = cv2.convertScaleAbs(self.image, alpha=alpha, beta = beta)
        self.image = new_image
        self.open_image()
    
    def saturation(self, koef):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        hsv[...,1] = hsv[...,1]*koef
        self.image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        self.open_image()
    
    def resize_img(self, height, width):
        size = (width, height)
        new_image = cv2.resize(self.image, size, interpolation = cv2.INTER_AREA)
        self.image = new_image
        self.open_image()
    
    def resize_prop(self, scale_percent):
        print(f"Original size: {self.image.shape}")
        width = int(self.image.shape[1] * scale_percent/100)
        height = int(self.image.shape[0] * scale_percent/100)
        size = (width, height)
        new_image = cv2.resize(self.image, size, interpolation = cv2.INTER_AREA)
        self.image = new_image
        print(f"Resized Dimensions: {self.image.shape}")
        self.open_image()
    
    def cropp(self, start_row, end_row, start_coll, end_coll):
        self.image = self.image[start_row:end_row, start_coll:end_coll]
        print(f"Resized Dimensions: {self.image.shape}")
        self.open_image()
    
    def rotate_image(self, angle):
        height, width = self.image.shape[:2]
        center_x, center_y = (width/2, height/2)
        matrix = cv2.getRotationMatrix2D((center_x, center_y), angle, 0.5)
        self.image = cv2.warpAffine(self.image, matrix, (width, height))
        self.open_image()


editor_1 = Editor(name_img, 'forest_rotate.jpg')
editor_1.open_image()
editor_1.cropp(600, 900, 1000, 1600)
editor_1.rotate_image(90)