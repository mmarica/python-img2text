from argparse import ArgumentParser

class CmdArgs(object):
    def __init__(self):
        parser = ArgumentParser(description='Convert an image into ASCII art')
        parser.add_argument('filename', type=str,
                            help='image file name')
        parser.add_argument('--downscale', type=int, dest='downscale', default=5,
                            help='downscale factor (how many times the image should be scaled down before transforming each pixel into a text character)')
        parser.add_argument('--hmul', type=float, dest='hmul', default=0.6,
                            help='multiplier for height when resizing (can be used to compensate for the shape of the console characters, which are taller than wider)')
        self.parser = parser

    def getArgs(self):
        args = self.parser.parse_args()
        return (args.filename, args.downscale, args.hmul)
