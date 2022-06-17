from PIL import Image
from PIL.ExifTags import TAGS
import sys

def get_data(image_fn):
    try:
        image = Image.open(image_fn)  
        exifdata = image.getexif()
        for tagid in exifdata:
              
            # getting the tag name instead of tag id
            tagname = TAGS.get(tagid, tagid)
          
            # passing the tagid to get its respective value
            value = exifdata.get(tagid)
            
            # printing the final result
            print(f"{tagname:25}: {value}")
    except:
        print(f"Failed to get data from {image_fn}")

if len(sys.argv) == 1:
    print("Give photo to extract as command line argument.")
    exit(0)

for i in range(1, len(sys.argv)):
    header = f"+=== DATA FROM {sys.argv[i]} ===+"
    print(header)
    get_data(sys.argv[i])
    print('+' + "="*(len(header)-2) + '+')


