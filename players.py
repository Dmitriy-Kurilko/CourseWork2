class Player:
    def __init__(self, user_name, words_which_use_user=[]):
        self.user_name = user_name
        self.words_which_use_user = words_which_use_user

    def get_quantity_words(self):
        return len(self.words_which_use_user)

    def add_word_in_list(self, any_word):
        self.words_which_use_user.append(any_word)

    def check_use_word_recent(self, any_word):
        return any_word in self.words_which_use_user

    def __repr__(self):
        return f'{self.user_name} {self.words_which_use_user}'
