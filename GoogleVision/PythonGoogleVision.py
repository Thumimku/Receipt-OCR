import argparse
import io
import tempfile
import os.path


from google.protobuf.json_format import MessageToJson
from PIL import Image
from google.cloud import vision
from google.cloud.vision import types


def main(image_file):
    # Instantiates a client]
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    labels = response.text_annotations

    for label in labels:
        print(label.description)
        save_file(label.description, completeName)

    print(format(labels[0].description))



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



def save_file(data_text,file_name):
    file_object = open(file_name, "w")
    file_object.write(data_text)
    file_object.close()

save_path = "/home/chukku/PycharmProjects/Receipt-OCR/Evaluation"
completeName = os.path.join(save_path, "outputG"+".txt")
main('test.png')
