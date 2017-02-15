from argparse import ArgumentParser

class CmdArgs(object):
    def __init__(self, default_downscale, default_height_multiplier, default_inverted):
        parser = ArgumentParser(description='Convert an image into ASCII art')
        parser.add_argument('filename', type=str,
                            help='image file name')
        parser.add_argument('--downscale', type=int, dest='downscale', default=default_downscale,
                            help='downscale factor (how many times the image should be scaled down before transforming each pixel into a text character)')
        parser.add_argument('--height_multiplier', type=float, dest='height_multiplier', default=default_height_multiplier,
                            help='multiplier for height when resizing (can be used to compensate for the shape of the console characters, which are taller than wider)')
        parser.add_argument('--inverted', type=bool, dest='inverted', default=default_inverted,
                            help='use True for displaying the generated ASCII image with white characters black on background, or False otherwise')
        self.parser = parser

    def getArgs(self):
        args = self.parser.parse_args()
        return (args.filename, args.downscale, args.height_multiplier, args.inverted)
