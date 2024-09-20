
#%matplotlib inline
import numpy as np
import cv2
from matplotlib import pyplot as plt
from urllib.request import urlopen, Request
def img_via_url():
    # Returns a Numpy Array with RGB colors
    URL = "https://upload.wikimedia.org/wikipedia/commons/0/02/Sea_Otter_%28Enhydra_lutris%29_%2825169790524%29_crop.jpg"
    HEADER = {'User-Agent': 'Mozilla/5.0'}
    
    # TODO: Fill out the withstatement below to fetch an image and make it a numpy array in RGB colors
    with urlopen(URL) as req:
        arr =  np.asarray(bytearray(req.read()), dtype=np.uint8)
        BGR_img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        
    RGB_img =  cv2.cvtColor(BGR_img, cv2.COLOR_BGR2RGB)
        
    return RGB_img

img = img_via_url()

# To show our img
plt.imshow(img)
plt.show()

def copy_and_process(img):
    img_copy =  img.copy() 
    resized_img = cv2.resize(img_copy, (256, 256)) 
    
    # Get original dimensions (height, width)
    height, width = img.shape[:2] 
    
    # Return resized image, original height, and original width
    return resized_img, height, width

resized_img, height, width = copy_and_process(img)

print(f"Width of resized img: {width}, height of resized img: {height}")
print(f"First 4 columns in the first row: {resized_img[0][:4]}")
plt.imshow(resized_img)
plt.show()
def set_pixel_values(resized_img, width, height):
    """Color the left half of the bottom side red and the right half green."""
    
    for row in range(width):  
        for column in range(height):  
            prev_val = resized_img[column][row]
            
            if column >= height // 2:
                if row < width // 2:
                    resized_img[column][row] = [255, prev_val[1], prev_val[2]]  # Red
                else:
                    resized_img[column][row] = [prev_val[0], 255, prev_val[2]]  # Green

set_pixel_values(resized_img, resized_img.shape[1], resized_img.shape[0])

plt.imshow(resized_img)
plt.show()

flattened_img =  resized_img.reshape(-1)

print(flattened_img.shape)
print(flattened_img)