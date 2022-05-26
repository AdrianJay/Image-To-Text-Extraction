from pickle import DICT
from matplotlib.pyplot import text
from pyparsing import Dict
import pytesseract
from pytesseract import Output
import PIL.Image
import cv2

print("Type filename")
filename = input(":")
myconfig = r"==psm 2 ==oem 3"

text = pytesseract.image_to_string(PIL.Image.open(filename), config=myconfig)
#print(logos)

img = cv2.imread(filename)
height, width, channels = img.shape

data = pytesseract.image_to_data(img, config = myconfig, output_type = Output.DICT)

#print(data['logos'])
