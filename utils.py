import random
import requests
from basic_word import BasicWord


def get_json():
    response = requests.get("https://api.npoint.io/8d3c64c5176bf16c9a16", verify=False).json()
    word = random.choice(response)
    return BasicWord(word["word"], word["subwords"])
