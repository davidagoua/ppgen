from services.create_image import create_image_with_text

if __name__ == '__main__':
    img = create_image_with_text("HW", width=300, height=300, color="red", text_color="white")

    img.save("test.png")

