# -*- coding: utf8 -*-

import sys
from PIL import Image

class Img2Text(object):
    # image filename
    filename = ''
    # how many times the image should be scaled down before transforming each pixel into a text character
    downscale = 15

    def __init__(self, filename):
        self.filename = filename

    def pixel_to_char(self, rgb):
        # list of available characters, sorted by luminosity: darker to lighter
        chars = (" ", "░", "▒", "▓", "█")

        r, g, b = rgb
        luminance = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        return chars[int((len(chars)) * luminance / 255) - 1]

    def convert(self):
        # maximum image size allowed
        max_width = 2000
        max_height = 2000

        height_multiplier = 0.6

        try:
            img = Image.open(self.filename)
            width, height = img.size

            print "Image loaded successfully: %ix%i px" % (width, height)
        except Exception, e:
            print "[ERROR] Cannot load image file '%s': %r" % (self.filename, e)
            sys.exit(1)

        if width > max_width or height > max_height:
            print "[ERROR] Image larger than allowed size of %ix%i px" % (max_width, max_height)
            sys.exit(1)

        size = (width / self.downscale, int(height * height_multiplier / self.downscale))
        print "Downscale factor %i, height multiplier %0.1f, new size: %ix%i px" % (
        self.downscale, height_multiplier, size[0], size[1])

        resized_img = img.resize(size, Image.ANTIALIAS).convert('RGB');

        output = ""
        for y in range(size[1]):
            for x in range(size[0]):
                output += self.pixel_to_char(resized_img.getpixel((x, y)))
            output += "\n"

        return output


