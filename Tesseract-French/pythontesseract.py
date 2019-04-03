import tempfile

import imutils as imutils
from PIL import Image
import pytesseract
import cv2
import numpy as np
import os.path




def save_file(data_text,file_name):
    file_object = open(file_name, "w")
    file_object.write(data_text)
    file_object.close()


# set dpi to 300 and save it as temp file using Image lib
def set_image_dpi(file_path):
    im = Image.open(file_path)
    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False,   suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename


# rescale image to 300 dpi in CV2
def rescale_image(file_path,image_save_path):
    img = cv2.imread(file_path)
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(image_save_path+"/test_rescaled.png",img)
    return img


# noise removal thorugh cv2
def noise_removal(img,image_save_path):
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=10)
    img = cv2.erode(img, kernel, iterations=1)

    # Apply blur to smooth out the edges
    img = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite(image_save_path+"/test_noise_removed.png",img)
    return img

# noise removal thorugh cv2
def noise_removal_without_saving(img):
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=10)
    img = cv2.erode(img, kernel, iterations=1)

    # Apply blur to smooth out the edges
    img = cv2.GaussianBlur(img, (5, 5), 0)
    return img

# binarisation thorugh cv2
def binarization(img,image_save_path):
    # Apply threshold to get image with only b&w (binarization)
    retval, threshold = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    cv2.imwrite(image_save_path+"/test_binarized.png", threshold)

    return img


save_path = "/home/thumilan/Desktop/FYP/Evaluation"
image_save_path = "/home/thumilan/Desktop/FYP/ProcessedImage"
completeName = os.path.join(save_path, "output"+".txt")

# data_text = pytesseract.image_to_string(Image.open(set_image_dpi('test2.png')), lang='fra')

img = cv2.imread('test.png')
cv2.imwrite(image_save_path+"/test.png", img)

data_text = pytesseract.image_to_string(binarization(noise_removal(rescale_image('test.png', image_save_path), image_save_path), image_save_path), lang='fra')

save_file(data_text, completeName)

# detect_text_block_with_skew('/home/thumilan/Desktop/FYP/Tesseract-French/test.png')