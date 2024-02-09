from gamer import Player
from utils import get_json


def main():
    word = get_json()
    user_name = input('Ввведите имя игрока: ')
    player = Player(user_name, [])

    print(f'Привет, {user_name}!')
    print(f'Составьте {len(word.list_with_words)} слов из слова {word.word}')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop/стоп"')
    print('Поехали, ваше первое слово?')

    while len(player.used_words) != len(word.list_with_words):
        user_word = input('Твое слово: ')
        if user_word.lower() in ['stop', 'стоп']:
            print(f'Игра завершена, вы угадали {len(player.used_words)} слов!')
            break

        if len(user_word) < 3:
            print('Слишком короткое слово')
        elif player.checker(user_word):
            print('Уже использовано')
        elif user_word in word.list_with_words:
            player.used_words.append(user_word)
            print('Верно')
        elif len(user_word) > len(word.word):
            print('Слишком длинное слово')
        else:
            print('Неверно')


if __name__ == '__main__':
    main()
