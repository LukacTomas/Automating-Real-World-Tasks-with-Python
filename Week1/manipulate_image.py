#!/usr/bin/env python3
# Google IT Automation with Python Professional Certificate
# Tomas Lukac
# 2021/11/3

from PIL import Image
import os
import os.path
from datetime import datetime


def get_images_from_dir(dir='.', allowed_types=["", ".png", ".jpg", ".jpeg", ".bmp", ".webp", ".tiff"]):
    """ Function for getting all images from current directory
    Args:
        dir (string): Set the working directory.
        allowed_types (list)): List of allowed image types -[".png", ".jpg", ".jpeg", ".bmp", ".webp"] .
    """
    images = []
    for file in os.listdir(dir):
        extension = os.path.splitext(file)[1]
        print(extension)
        if extension.lower() not in allowed_types:
            continue
        images.append(file)
    return images


def resize_image(image, resize_size=(128, 128)):
    """ Function resize_image for resizing `image` object
    Args:
        image (object): Image object from PIL.
        rezize_size (Tupple)): Resize size = default is (128, 128).
    """
    return image.resize(resize_size)


def rotate_image(image, degrees=0):
    """ Function rotate_image for rotating `image` object
    Args:
        image (object): Image object from PIL.
        degrees (number)): Degrees of rotation = default is 0.
    """
    return image.rotate(degrees)


def save_image(image, destination='', extension="jpeg"):
    """Simple function for saving image object to destination
       Args:
       image (object): Image object from PIL.
       destination (string): String that represents dir and filename
    """
    # check if destination already exists
    # if exist add timestamp to destination name
    if destination == "":
        raise Exception("Destination cannot be empty")

    if os.path.isfile(destination):
        timestamp = int(datetime.now().timestamp())
        dest_array = os.path.splitext(destination)
        destination = dest_array[0] + str(timestamp) + "." + extension
    else:
        destination = os.path.splitext(destination)[0] + "." + extension

    image.save(destination, format=extension)


if __name__ == "__main__":
    dest = ""
    images = get_images_from_dir()
    dir = "./opt/icons/"
    if not os.path.exists(dir):
        os.makedirs(dir)

    for image in images:
        extension = os.path.splitext(image)[1]
        with Image.open(dest + image).convert('RGB') as im:
            im = rotate_image(im, 270)
            im = resize_image(im, (128, 128))
            save_image(im, dir + image)
