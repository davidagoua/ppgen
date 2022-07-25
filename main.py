from fastapi import FastAPI, responses
from uuid import uuid4
from services.create_image import create_image_with_text
from services.short_name import short_name, increment_in_file, get_counter_from_file

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/image/{text}")
async def create_image(text: str, width: int = 200, height: int = 200, color: str = "white", text_color: str = "black"):
    name = short_name(text).upper()
    img = create_image_with_text(name, width, height, color, text_color)
    name = "./images/" + str(uuid4()) + "test.png"
    image = img.save(name)
    increment_in_file("counter.txt")
    return responses.FileResponse(name)


@app.get('/counter')
async def get_counter():
    return {"counter": get_counter_from_file("counter.txt")}


