import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'Path to the tesseract.exe'
from PIL import Image

img = Image.open('learn.png')

text = tess.image_to_string(img);

print(text)
