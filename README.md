## RGB image to RGB565 C matrix conversion
I used this script to quickly convert small RGB images to C RGB565 matrices for some projects with microcontrollers.\
It is not meant to be a complete conversion, but it is enough for my purposes.\
It read every pixel of the image and prints the 16 bit RGB565 value on the standard output. I sujest to redirect the output to a file.

### Usage
```
git clone git@github.com:davideaimar/RGB888-to-RGB565matrix.git
cd RGB888-to-RGB565matrix
pip install -r requirements.txt
python3 main.py -i <path/to/input/file> > out.txt
```