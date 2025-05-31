import os
import base64
from openai import OpenAI
from check_for_key import has_key
from instructions import prompt, model_instruction

client = OpenAI() #gets OPENAI_API_KEY from env variable as default

def set_id(num) -> str:
    return str(num).zfill(3)

def get_image_path(id: str) -> str:
    base_dir = os.path.dirname(__file__)
    img_path = os.path.join(base_dir, "images", f"{id}.jpg")

    if not os.path.isfile(img_path):
        raise FileNotFoundError(f"Image file not found: {img_path}")
    else:
        return img_path

def get_response_file_path() -> str:
    base_dir = os.path.dirname(__file__)
    response_dir = os.path.join(base_dir, "responses")
    os.makedirs(response_dir, exist_ok=True)
    return os.path.join(response_dir, "responses.txt")

def get_description_file_path(id: str) -> str:
    base_dir = os.path.dirname(__file__)
    description_dir = os.path.join(base_dir, "descriptions")
    os.makedirs(description_dir, exist_ok=True)
    return os.path.join(description_dir, f"{id}.txt")

def img_to_description(img_path: str) -> list:
    with open(img_path, "rb") as image_file:
        b64_image = base64.b64encode(image_file.read()).decode("utf-8")

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=model_instruction,
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"},
                ],
           }
        ],
    )
    return response

#main
if __name__ == "__main__":
    if not has_key():
        print("No OPENAI_API_KEY is set.")
    start_num: int = 0                                        #int(input("Input starting number (inclusive): "))
    num_of_images: int = 1                                      #int(input("Input number of pictures: "))
    response_path = get_response_file_path()

    for image in range(num_of_images):
        num_for_id: int = start_num + image
        id: str = set_id(num_for_id)
        description__path = get_description_file_path(id)

        print(f"Analyse {id}.jpg")
        response = img_to_description(get_image_path(id))

        with open(response_path, "a") as f: #save entire response object
            f.write(f"Response of {id}.jpg: {response}\n")

        with open(description__path, "w") as f: #save the actual answer
            f.write(f"Description of {id}.jpg: \n {response.output[0].content[0].text}\n")

        print(f"Done with {id}.jpg")
    print(f"Done with all (from {start_num}to{start_num+num_of_images})")