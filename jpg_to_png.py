import os
from PIL import Image

def jpg_to_png(input_folder,output_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith(".jpg"):
                with Image.open(os.path.join(input_folder,filename)) as img:
                    png_name = filename.replace(".jpg",".png")
                    img.save(os.path.join(output_folder,png_name), "PNG")
                    print(f'{filename}:::{png_name}')

jpg_to_png("pokedex","new")






