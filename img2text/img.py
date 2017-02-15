# -*- coding: utf8 -*-

import sys
from PIL import Image

class Img2Text(object):
    # list of available characters, sorted by luminosity: darker to lighter
    chars = (" ", "░", "▒", "▓", "█")

    # maximum image size allowed
    max_width = 2000
    max_height = 2000

    # image object
    image = None

    # image filename
    filename = ''
    # how many times the image should be scaled down before transforming each pixel into a text character
    downscale = 5
    # multiplier for height when resizing, to compensate for the console characters shape, which are taller than wider
    height_multiplier = 0.6

    def __init__(self, filename):
        self.filename = filename

    def convert(self):
        self.load_image()
        width, height = self.image.size

        size = (width / self.downscale, int(height * self.height_multiplier / self.downscale))
        print "Downscale factor %i, height multiplier %0.1f, new size: %ix%i px" % (self.downscale, self.height_multiplier, size[0], size[1])

        resized_img = self.image.resize(size, Image.ANTIALIAS).convert('RGB');

        output = ""
        for y in range(size[1]):
            for x in range(size[0]):
                output += self.pixel_to_char(resized_img.getpixel((x, y)))
            output += "\n"

        return output

    def load_image(self):
        try:
            self.image = Image.open(self.filename)
            width, height = self.image.size

            print "Image loaded successfully: %ix%i px" % (width, height)
        except Exception, e:
            print "[ERROR] Cannot load image file '%s': %r" % (self.filename, e)
            sys.exit(1)

        if width > self.max_width or height > self.max_height:
            print "[ERROR] Image larger than allowed size of %ix%i px" % (self.max_width, self.max_height)
            sys.exit(1)

    def pixel_to_char(self, rgb):
        r, g, b = rgb
        luminance = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        return self.chars[int((len(self.chars)) * luminance / 255) - 1]
