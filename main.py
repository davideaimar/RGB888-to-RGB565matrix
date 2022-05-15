from PIL import Image

def rgb_to_16bit(r, g, b):
    return ( (( r   >> 3 ) << 11 ) | (( g >> 2 ) << 5  ) | ( b  >> 3 ))


im = Image.open('land-input.png', 'r')

width, height = im.size

pix_val = list(im.getdata())

for i in range(len(pix_val)):
    pix_val[i] = rgb_to_16bit(pix_val[i][0], pix_val[i][1], pix_val[i][2])

print(f'uint16_t pipe[{height}][{width}] = {{')
for y in range(height):
    print('{')
    for x in range(width):
        print(f'{hex(pix_val[y*width + x])}, ', end='')
    print('}, ', end='')
    print(f'// line {y}')
print('};')