"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_HEIGHT = 1792
PATCH_WIDTH = 828
WIDTH = N_COLS * PATCH_WIDTH
HEIGHT = N_ROWS * PATCH_HEIGHT
PATCH_NAME = 'images/IMG_3221.png'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # This is an example which should generate a pinkish patch

    for row in range(N_ROWS):
        for col in range(N_COLS):
            patch = make_recolored_patch(row, col, random.randint(1, 2))
            paste_recolored_patch(final_image, patch, col, row)

    final_image.show()

def paste_recolored_patch(final_image, patch, col, row):
    # by this function I get a recolored patch pasted into final image
    # I input two values and get back one
    for y in range(patch.height):
       for x in range(patch.width):
            original_file = patch.get_pixel(x, y)
            final_image.set_pixel(x + col * PATCH_WIDTH, y + row * PATCH_HEIGHT, original_file)
    return final_image

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
            pixel.red *= red_scale
            pixel.green *= green_scale
            pixel.blue *= blue_scale
    return patch

if __name__ == '__main__':
    main()