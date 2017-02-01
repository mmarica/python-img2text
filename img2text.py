from PIL import Image
import sys

downscale = 5

if len(sys.argv) != 2:
    print "Please specify an image file/url"
    sys.exit(1)


filename = sys.argv[1]

try:
    img = Image.open(filename)
    width, height = img.size

    print "Image loaded successfully: %ix%i px" % (width, height)
except Exception, e:
    print "[ERROR] Cannot load image file '%s': %r" % (filename, e)
    sys.exit(1)

size = (width / downscale, height / downscale)
print "Downscale factor %i, new size: %ix%i px" % (downscale, size[0], size[1])


resized_img = img.resize(size, Image.ANTIALIAS)
new_img = Image.new(mode='RGBA', size=size, color=(255, 255, 255, 0));
new_img.paste(resized_img, (0, 0));
new_img.save('test.png')
