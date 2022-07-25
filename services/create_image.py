from PIL import Image, ImageDraw, ImageFont


def create_image(width, height, color) -> Image:
    """
    Create an image with the given width, height and color.
    """
    image = Image.new('RGB', (width, height), color)
    return image


def create_image_with_text(text, width=200, height=200, color="white", text_color="black") -> Image:
    """
    Create an image with the given width, height and color.
    """
    text_size = width // len(text) - 10
    image = Image.new('RGBA', (width, height), color)
    font = ImageFont.truetype("arial.ttf", text_size)
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(text, font=font)
    draw.text(((width-w)/2,(height-h)/2), text, fill=text_color, font=font)
    return image