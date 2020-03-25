import os
import pytesseract
import time
from tqdm import tqdm
from pdf2image import convert_from_path
try:
    from PIL import Image
except ImportError:
    import Image

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
TRAINING_DATA_DIR = PROJECT_DIR + "/training_data"
RAW_DATA_DIR = PROJECT_DIR + "/raw_data"

# get training data that are in pdf
for i in os.listdir(TRAINING_DATA_DIR):
    
    # create a newfolder that contains all the pages of this file
    des_file_dir = f"{RAW_DATA_DIR}/{i}"
    try:
        os.mkdir(des_file_dir)
    except FileExistsError:
        print(f"'{i}' already exists, continuing!")

    # get the absolute path of current file and open it
    src_file_dir = f"{TRAINING_DATA_DIR}/{i}"

    images = convert_from_path(src_file_dir, jpegopt='jpeg')
    pbar = tqdm(total=100)
    pbar_len = (100 // len(images))
    for file_number, j in enumerate(images):
        
        # for loading bar
        time.sleep(0.5)
        pbar.update(pbar_len)
        file_name = f"{des_file_dir}/{file_number}.jpeg"
        
        # creating image from pdf
        new_file = open(file_name, "w")
        j.save(new_file)
        new_file.close()

        # getting text from this image
        text = pytesseract.image_to_string(Image.open(file_name))
        result_file = open(f"{des_file_dir}/{file_number}.txt", "w")
        result_file.write(text)
        result_file.close()
        os.remove(f"{des_file_dir}/{file_number}.jpeg")
    
    pbar.close()

print(f"Read {len(os.listdir(TRAINING_DATA_DIR))} file\\s")