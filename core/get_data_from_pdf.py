import os
import pytesseract
import time
import math
from tqdm import tqdm
from pdf2image import convert_from_path
try:
    from PIL import Image
except ImportError:
    import Image

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
TRAINING_DATA_DIR = PROJECT_DIR + "/training_data"
RAW_DATA_DIR = PROJECT_DIR + "/raw_data"

#creating a file for the final output
result_file = open(f"{RAW_DATA_DIR}/raw_data.txt", "a+")
        
# get training data that are in pdf
for i in os.listdir(TRAINING_DATA_DIR):
    #get the path for the curr file
    src_file_dir = f"{TRAINING_DATA_DIR}/{i}"

    #convert this pdf file into images (one image per page)
    images = convert_from_path(src_file_dir, jpegopt='jpeg')

    pbar = tqdm(total=100)
    pbar_len = math.ceil(100 // len(images))

    for j in images:
        
        # for loading bar
        time.sleep(0.5)
        pbar.update(pbar_len)

        file_name = f"{RAW_DATA_DIR}/temp.jpeg"
        
        # creating image from pdf
        new_file = open(file_name, "w")
        j.save(new_file)
        new_file.close()

        # getting text from this image and \
        # appending it to the result file
        text = pytesseract.image_to_string(Image.open(file_name))
        result_file.write(text)
        
        #removing the left over image(temp) file
        os.remove(f"{RAW_DATA_DIR}/temp.jpeg")

#closing the raw data file
result_file.close()

pbar.close()

print(f"Read {len(os.listdir(TRAINING_DATA_DIR))} file\\s")