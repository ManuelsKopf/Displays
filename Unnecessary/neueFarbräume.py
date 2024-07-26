# passt
# Python program to explain cv2.cvtColor() method 

# importing cv2 
import cv2 
import matplotlib.pyplot as plt

# path 
path = "Base pictures\Image1.jpeg"

# Reading an image in default mode 
src = cv2.imread(path) 



# Using cv2.cvtColor() method 
# Using cv2.COLOR_BGR2GRAY color space 
# conversion code 
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY ) 

# Displaying the image 
#cv2.imshow(window_name, image) 
plt.imshow(image)
plt.show()

image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
plt.imshow(image)
plt.show()