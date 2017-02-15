from img2text.cmd import *
from img2text.img import *

args = CmdArgs(Img2Text.DEFAULT_DOWNSCALE,
               Img2Text.DEFAULT_HEIGHT_MULTIPLIER,
               Img2Text.DEFAULT_INVERTED)
filename, downscale, height_multiplier, inverted = args.getArgs()

img = Img2Text(filename)
print img.downscale(downscale)\
    .height_multiplier(height_multiplier)\
    .inverted(inverted)\
    .convert()
