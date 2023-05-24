import random
import requests
from basic_word import BasicWord


def load_random_word():
    list_with_words = requests.get('https://www.jsonkeeper.com/b/7U5N').json()
    result = random.choice(list_with_words)
    basic_word = BasicWord(result['word'], result['subwords'])
    return basic_word


result = load_random_word()
