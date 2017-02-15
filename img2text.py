from img2text.cmd import *
from img2text.img import *

# multiplier for height when resizing, to compensate for the console characters shape, which are taller than wider

args = CmdArgs()
filename, downscale, height_multiplier = args.getArgs()

img = Img2Text(filename)
print img.convert()

