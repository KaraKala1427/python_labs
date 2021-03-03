import logging
import azure.functions as func
import io
import sys
from PIL import Image


FINAL_COMPOSITE_MAX_HEIGHT = 700
FINAL_COMPOSITE_MAX_WIDTH = 700

burger_WIDTH_RATIO = 7

def main(blobin: func.InputStream, blobout: func.Out[bytes], context: func.Context):
    logging.info(f"--- Python blob trigger function processed blob \n"
                 f"----- Name: {blobin.name}\n"
                 f"----- Blob Size: {blobin.length} bytes")
    

    input_image = blobin
    burger_image = f'{context.function_directory}/burger.png'

    try:
        base_image = Image.open(input_image)
        burger = Image.open(burger_image)
    except OSError as e:
        print(f'EXCEPTION: Unable to read input as image. {e}')
        sys.exit(254)
    except Exception as e:
        print(f'EXCEPTION: {e}')
        sys.exit(255)

  
    if base_image.width > FINAL_COMPOSITE_MAX_WIDTH or base_image.height > FINAL_COMPOSITE_MAX_HEIGHT:
        if base_image.height > base_image.width:
            factor = 900 / base_image.height
        else:
            factor = 900 / base_image.width
        base_image = base_image.resize((int(base_image.width * factor), int(base_image.height * factor)))

 
    relative_ws = round(base_image.width/burger_WIDTH_RATIO)
    burger_size = (relative_ws, relative_ws)
    burger.thumbnail(burger_size, Image.ANTIALIAS)


    position = (16, 16)
    
    img = Image.new('RGBA', (base_image.width, base_image.height), (0, 0, 0, 0))
    img.paste(base_image, (0, 0))

    try:
        img.paste(burger, position, mask=burger)
    except ValueError:
        img.paste(burger, position)

    img.show()


    img_byte_arr = io.BytesIO()

    img.convert('RGB').save(img_byte_arr, format='JPEG')

    blobout.set(img_byte_arr.getvalue())

    logging.info(f"----- burgering successful")