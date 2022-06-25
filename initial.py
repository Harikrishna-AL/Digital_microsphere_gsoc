import numpy as np
import cv2 
import cv as cv
import pandas as pd
from skimage import io
from PIL import Image
import matplotlib.pylab as plt

def resize(image):
    resized_image = cv2.resize(image,(0,0),fx=0.3,fy=0.3)
    return resized_image

def blur(img):
    pass
def outline(image):
    pass
def mask(image):
    pass

