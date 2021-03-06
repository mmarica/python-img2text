# -*- coding: utf8 -*-

import sys
from PIL import Image

class Img2Text(object):
    # list of available characters, sorted by luminosity: darker to lighter (assuming light text on dark background)
    chars = (" ", "░", "▒", "▓", "█")

    # defaults
    DEFAULT_DOWNSCALE = 5
    DEFAULT_HEIGHT_MULTIPLIER = 0.6
    DEFAULT_INVERTED = True

    # maximum image size allowed
    MAX_WIDTH = 2000
    MAX_HEIGHT = 2000

    # image filename
    filename = ''
    # how many times the image should be scaled down before transforming each pixel into a text character
    downscale = DEFAULT_DOWNSCALE
    # multiplier for height when resizing, to compensate for the console characters shape, which are taller than wider
    height_multiplier = DEFAULT_HEIGHT_MULTIPLIER
    # use True for displaying the generated ASCII image with black characters on white background
    inverted = DEFAULT_INVERTED

    def __init__(self, filename):
        self.filename = filename

    def downscale(self, downscale):
        self.downscale = downscale
        return self

    def height_multiplier(self, height_multiplier):
        self.height_multiplier = height_multiplier
        return self

    def inverted(self, inverted):
        self.inverted = inverted
        return self

    def convert(self):
        image = self.__load_image()
        width, height = image.size

        size = (width / self.downscale, int(height * self.height_multiplier / self.downscale))
        resized_img = image.resize(size, Image.BICUBIC).convert('RGB');

        output = ""
        for y in range(size[1]):
            for x in range(size[0]):
                output += self.__pixel_to_char(resized_img.getpixel((x, y)))
            output += "\n"

        return output

    def __load_image(self):
        try:
            image = Image.open(self.filename)
            width, height = image.size
        except Exception, e:
            print "[ERROR] Cannot load image file '%s': %r" % (self.filename, e)
            sys.exit(1)

        if width > self.MAX_WIDTH or height > self.MAX_HEIGHT:
            print "[ERROR] Image larger than allowed size of %ix%i px" % (self.MAX_WIDTH, self.MAX_HEIGHT)
            sys.exit(1)

        return image

    def __pixel_to_char(self, rgb):
        r, g, b = rgb
        luminance = int(0.299*r + 0.587*g + 0.114*b)

        if self.inverted:
            luminance = 255 - luminance

        return self.chars[int((len(self.chars) - 1) * luminance / 255)]
