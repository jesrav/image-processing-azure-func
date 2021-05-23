from io import BytesIO

from PIL import Image


def crop_image(
    image: Image, left_margin: float, top_margin: float, width: float, height: float
) -> Image:
    """Crop image
    ----------
    image: Pillow image.
    xmin: x minimum for the cropping area. between 0 and 1.
    ymin: y minimum for the cropping area. between 0 and 1.
    width: Width between 0 and 1.
    height: Heigh between 0 and 1.
    Returns
    -------
    Cropped pillow image
    """
    img_width, img_height = image.size

    left = int(left_margin * img_width)
    right = int((left_margin + width) * img_width)
    top = int(top_margin * img_height)
    bottom = int((top_margin + height) * img_height)
    return image.crop((left, top, right, bottom))


def pil_image_to_byte_array(image: Image, format: str = "jpeg") -> bytes:
    """Convert Pillow image to byte array."""
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format=image.format or format)
    return img_byte_arr.getvalue()