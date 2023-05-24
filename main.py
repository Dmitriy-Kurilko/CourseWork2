from utils import result
from players import Player


def start_game():
    user_name = input('Привет! Для начала игры напиши, как тебя зовут? ')
    player = Player(user_name)
    lst = [f'Составьте {result.counter_len_acceptable_list()} слов из слова {result.main_word}',
           'Слова должны быть не короче 3 букв',
           'Чтобы закончить игру, угадайте все слова или напишите "stop"']

    for i in lst:
        print(i)

    while len(player.words_which_use_user) < result.counter_len_acceptable_list():
        user_input = input('Введите слово ')
        if user_input.lower() in ['stop', 'стоп'] or len(player.words_which_use_user) == len(result.acceptable_list):
            print(f'Игра завершена, вы угадали {len(player.words_which_use_user)} слов!')
            break

        if len(user_input) < 3:
            print('Слишком короткое слово')
        elif user_input not in player.words_which_use_user and user_input in result.acceptable_list:
            player.add_word_in_list(user_input)
            print('Верно! Идем дальше')
        elif user_input in player.words_which_use_user:
            print('Уже использовано')
        else:
            print('Неверно')


start_game()
