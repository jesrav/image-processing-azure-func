from io import BytesIO
import logging

import azure.functions as func
from PIL import Image

from image_processor.image_processing import crop_image, pil_image_to_byte_array

def main(
    imageinput: func.InputStream,
    croppedimageoutput: func.Out[bytes]
    ):
    logging.info(
        f"Prossecing blob"
        f"Name: {imageinput.name}\n"
        f"Blob Size: {imageinput.length} bytes")
    image = Image.open(BytesIO(imageinput.read()))
    image_cropped = crop_image(
        image=image, 
        left_margin=0.2, 
        top_margin=0.1,
        width=0.6, 
        height=0.7
    )
    croppedimageoutput.set(
        pil_image_to_byte_array(image_cropped)
    )
    
