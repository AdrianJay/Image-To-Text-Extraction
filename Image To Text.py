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

amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 80:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
        img = cv2.putText(img, data['text'][i], (x, y + height + 20 ), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("image", img)
cv2.waitKey(0)
