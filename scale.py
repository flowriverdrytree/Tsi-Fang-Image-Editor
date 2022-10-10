#!/usr/bin/env python
# This script take a directory path as the input, and scale all images under into 75px
# 1000px width for Landsacpe images, and 800px width for Portrait images.

# import modules used here -- sys is a very standard one
import os, argparse
from os.path import join, exists, isdir, realpath
from PIL import Image

# Gather our code in a main() function
def main(args):
  root_path = realpath(args.root)

  if not isdir(root_path):
      print("[Error] Invalid root path: {}".format(root_path))
      return
  
  print("Start scaling images under {} ...".format(root_path))

  # assume dir structure is root/name/image.jpg
  for (root, dirs, files) in os.walk(root_path, topdown=True):
      for file in files:
        file_path = join(root, file)
        if exists(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
          print(file_path)

          try:
            img = Image.open(file_path)
            img = apply_orientation(img)
            old_width, old_height = img.size
            old_size = img.size

            # expected width = 1000px on landscape mode, 800px on portrait mode, 
            new_width = 1000
            if old_height > old_width:  # portrait mode
              new_width = 800

            expected_size = (new_width, old_height)
            img.thumbnail(expected_size, Image.ANTIALIAS)
            img.save(file_path, dpi=(75, 75))

            print("Scaling image from {} to {}\n".format(old_size, img.size))
          except IOError:
            print("Fail to read/write image")
          except:
            print("Unknown image handling error")



def flip_horizontal(im): return im.transpose(Image.FLIP_LEFT_RIGHT)
def flip_vertical(im): return im.transpose(Image.FLIP_TOP_BOTTOM)
def rotate_180(im): return im.transpose(Image.ROTATE_180)
def rotate_90(im): return im.transpose(Image.ROTATE_90)
def rotate_270(im): return im.transpose(Image.ROTATE_270)
def transpose(im): return rotate_90(flip_horizontal(im))
def transverse(im): return rotate_90(flip_vertical(im))
orientation_funcs = [None,
                 lambda x: x,
                 flip_horizontal,
                 rotate_180,
                 flip_vertical,
                 transpose,
                 rotate_270,
                 transverse,
                 rotate_90
                ]

def apply_orientation(im):
    """
    https://stackoverflow.com/questions/4228530/pil-thumbnail-is-rotating-my-image
    Extract the oritentation EXIF tag from the image, which should be a PIL Image instance,
    and if there is an orientation tag that would rotate the image, apply that rotation to
    the Image instance given to do an in-place rotation.

    :param Image im: Image instance to inspect
    :return: A possibly transposed image instance
    """

    try:
        kOrientationEXIFTag = 0x0112
        if hasattr(im, '_getexif'): # only present in JPEGs
            e = im._getexif()       # returns None if no EXIF data
            if e is not None:
                # print('EXIF data found: %r', e)
                print("EXIF data found, rotate image if necessary")
                orientation = e[kOrientationEXIFTag]
                f = orientation_funcs[orientation]
                return f(im)
    except:
        # We'd be here with an invalid orientation value or some random error?
        print("oritention rotation fail")
    return im


# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(dest='root', help="root of the images directory")
  args = parser.parse_args()
  
  main(args)