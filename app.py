import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN')

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer " + api_key}

with open('./data/shortStoryNature.md', 'r') as file:
    input_string = file.read()

lines = input_string.splitlines()

counter = 0
modified_lines = []
for line in lines:
    if line != "":
        counter += 1
        currentNum = str(counter)
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        image_bytes = query({
            "inputs": line,
        })
        image = Image.open(io.BytesIO(image_bytes))
        image.save(f"./images/shortStory{currentNum}.jpg")

        modified_lines.append(line + "![text illustration](../images/shortStory"+ currentNum + ".jpg)")
        print(modified_lines)  

# Join the modified lines back into a single string with line breaks
    modified_string = "\n".join(modified_lines)

    with open('./data/shortStoryNature.md', 'w') as file:
        file.write(modified_string)

