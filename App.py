import os
import re
import shutil
import cv2

from pytesseract import pytesseract

path_to_tesseract = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pytesseract.tesseract_cmd = path_to_tesseract

path_to_images = ""

destinaton_path = "Destination"
testPath = "Destination/"

fileList = []
resultList = []

filesMap = {}

a = 1
b = 1

for root, dirs, files_names in os.walk(path_to_images):
    
    for file in files_names:
        file_name, file_extension = os.path.splitext(file)
        shutil.copy(os.path.join(root, file), os.path.join(destinaton_path, f"{a}{file_extension}"))

        filesMap[f"{a}{file_extension}"] = f"{file}"
        a += 1

for root, dirs, file_names in os.walk(testPath):
    #Iterate over each file_name in the folder
    for file_name in file_names:
        #Open image with PIL
        print(b, ". Görsel İşleniyor...")
        b += 1
        image=cv2.imread(testPath + file_name)
        text=pytesseract.image_to_string(image,lang="tur").lower()
        x = re.search("murat", text)

        if x:
            fileList.append(file_name)

if len(fileList) == 0:
    print("No files found")
        
else:
    print("Found files: ", fileList)

for file in fileList:
    resultList.append(filesMap[f"{file}"])

print("Result: ", resultList)

for root, dirs, file_names in os.walk(testPath):
    for file_name in file_names:
        os.remove(testPath + file_name)
        