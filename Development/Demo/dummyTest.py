import os
import pytesseract
from PIL import Image

"""
def get_image_path(image_name):
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "images/{}".format(image_name))
    return image_path
"""

#image_path = get_image_path("dummypic1.png")
_, _, files = next(os.walk("images"))
for i in range(len(files)):
    image_path = "images/dummypic{}.png".format(i + 1)
    image = Image.open(image_path)

    extracted_text = pytesseract.image_to_string(image, lang="eng")
    cleaned_text = extracted_text.strip()

    if not i:
        file1 = open("images_output.txt", "w")
    else:
        file1 = open("images_output.txt", "a")
    
    file1.write(cleaned_text)
    file1.write("\n")
    file1.write("\n")
    file1.close()
