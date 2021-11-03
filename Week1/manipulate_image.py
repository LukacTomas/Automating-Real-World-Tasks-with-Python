from PIL import Image
import os
import os.path

images = ["code1.png", "code2.png"]


def resize_image(image, rezize_size=(128, 128)):
    """ Function resize_image for resizing `image` object
    Args:
        image (object): Image object from PIL.
        rezize_size (Tupple)): Resize size = default is (128, 128).
     """
    return image.rezize(rezize_size)


def rotate_image(image, degrees=0):
    """ Function rotate_image for rotating `image` object
    Args:
        image (object): Image object from PIL.
        degrees (number)): Degrees of rotation = default is 0.
     """
    return image.rotate(degrees)


def get_images_from_dir(dir='.', allowed_types=[".png", ".jpg", ".jpeg", ".bmp", ".webp"]):
    """ Function for getting all images from current directory
    Args:
        dir (string): Set the working directory.
        allowed_types (list)): List of allowed image types -["png", "jpg", "jpeg", "bmp", "webp"] .
    """
    images = []
    for file in os.listdir(dir):
        extension = os.path.splitext(file)[1]
        print(extension, file, extension in allowed_types)
        if extension.lower() not in allowed_types:
            continue
        images.append(file)
    return images


if __name__ == "__main__":
    pass
