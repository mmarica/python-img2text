from img2text.cmd import *
from img2text.img import *

args = CmdArgs()
filename, downscale, height_multiplier = args.getArgs()

img = Img2Text(filename)
print img.downscale(downscale)\
    .height_multiplier(height_multiplier)\
    .convert()
