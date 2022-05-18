import argparse
import os.path
from PIL import Image

def rgb_to_16bit(r, g, b):
    return ( (( r   >> 3 ) << 11 ) | (( g >> 2 ) << 5  ) | ( b  >> 3 ))

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return Image.open(arg, 'r')

def process_image(im: Image.Image):

    if im.mode != 'RGB':
        im = im.convert('RGB')

    width, height = im.size

    pix_val = list(im.getdata())

    for i in range(len(pix_val)):
        pix_val[i] = rgb_to_16bit(pix_val[i][0], pix_val[i][1], pix_val[i][2])

    print(f'static const uint16_t image[{height}][{width}] = {{')
    for y in range(height):
        print('{')
        for x in range(width):
            print(f'{hex(pix_val[y*width + x])}, ', end='')
        print('}, ', end='')
        print(f'// line {y}')
    print('};')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a image in RGB888 to a C matrix in RGB565.')

    parser.add_argument("-i", "--input", dest="filename", required=True,
                    help="image input file", metavar="FILE",
                    type=lambda x: is_valid_file(parser, x))

    args = parser.parse_args()

    process_image(args.filename)