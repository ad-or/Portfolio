"""
This program generates the Warhol effect based on the image chosen by a user.
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3

def main():
    image_path = browse_file()
    image = store_image(image_path)
    img_width = image.width
    img_height = image.height
    image.show()

    final_width = N_COLS * img_width
    final_height = N_ROWS * img_height
    final_image = SimpleImage.blank(final_width, final_height)

    for row in range(N_ROWS):
        for col in range(N_COLS):
            patch = make_recolored_patch(image_path, row, col, 1)
            paste_recolored_patch(final_image, patch, row, col, img_width, img_height)

    final_image.show()

def browse_file():
    '''
    This function allows browsing for a file. It stores the file's path in 'image_path' and return 'image_path'
    '''
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    image_path = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    return image_path

def store_image(image_path):
    '''
    Using path for our image we copy the selected image to our script and return it to store it in variable 'image'
    '''
    image = SimpleImage(image_path)
    return image

def make_recolored_patch(image_path, red_scale, green_scale, blue_scale):
    '''
    This function makes a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(image_path)
    for pixel in patch:
            pixel.red *= red_scale
            pixel.green *= green_scale
            pixel.blue *= blue_scale
    return patch

def paste_recolored_patch(final_image, patch, row, col, img_width, img_height):
    '''
    This function pastes recolored patch into final image
    '''
    for y in range(patch.height):
       for x in range(patch.width):
            original_file = patch.get_pixel(x, y)
            final_image.set_pixel(x + col * img_width, y + row * img_height, original_file)
    return final_image

if __name__ == '__main__':
    main()