from PIL import Image
import os
import io

def rgb_to_brightness(pixels, version):
    R, G, B = pixels
    if version == 1:
        return ((R + G + B) / 3)
    elif version == 2:
        return ((max(R, G, B) + min(R, G, B)) / 2)
    elif version == 3:
        return ((0.21 * R) + (0.72 * G) + (0.07 * B))
    else: 
        print("Error, select a version between 1 and 3.")

os.chdir("..")
logo = os.path.abspath(os.curdir) + "/logo.jpg"

im = Image.open(logo)
print("Image succesfully loaded.")
print("Size: " + str(im.size) + "\nMode: " + str(im.mode))

pixel_array = [] 
for x in range(400):
    second_array = []
    for y in range(400):
        second_array.append(
            rgb_to_brightness(im.getpixel((x, y)), 1)
        )
    pixel_array.append(second_array)

print("\nSuccessfully loaded image into pixel array.")




