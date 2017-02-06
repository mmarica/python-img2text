from PIL import Image
import sys

downscale = 5
max_width = 1000
max_height = 1000

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

if width > max_width or height > max_height:
    print "[ERROR] Image larger than allowed size of %ix%i px" % (max_width, max_height)
    sys.exit(1)

size = (width / downscale, height / downscale)
print "Downscale factor %i, new size: %ix%i px" % (downscale, size[0], size[1])


resized_img = img.resize(size, Image.ANTIALIAS)
new_img = Image.new(mode='RGBA', size=size, color=(255, 255, 255, 0));
new_img.paste(resized_img, (0, 0));
new_img.save('test.png')
