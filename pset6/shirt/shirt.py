import sys
from PIL import Image, ImageOps


# expects two command line arguments
if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

name1, ext1 = sys.argv[1].split(".")
name2, ext2 = sys.argv[2].split(".")

ext = ["jpg", "jpeg", "png"]

if ext1 != ext2:
    sys.exit("Input and Output have different extensions")

elif ext1.lower() not in ext or ext2.lower() not in ext:
    sys.exit("Invalid extension for input or output")

# opens an image object

try:
    input_img = Image.open(sys.argv[1])
    shirt = Image.open("shirt.jpg")

except FileNotFoundError:
    sys.exit("Input does not exist")

# resize input image
resized_input_img = ImageOps.fit(input_img,shirt.size) 

# overlay the shirt on input_img
resized_input_img.paste(shirt,(0,0),shirt)

# save the updated input_img after the overlay as a new image called "output.jpg"
resized_input_img.save(sys.argv[2])






'''
Psuedo/notes

Command line arguments requirements

Image:
    - use Image library to open input mmuppet
    - resize and crop using ImageOps.fit (method, bleeed, centering use default values)
    - take the cs50 shirt image and overlay it on input image using Image.paste
    - save output image



'''