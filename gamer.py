class Player:
    def __init__(self, user_name, used_words):
        self.user_name = user_name
        self.used_words = used_words

    def get_quantity_words(self):
        return len(self.used_words)

    def add_new_word(self, user_word):
        self.used_words.append(user_word)

    def checker(self, user_word):
        return user_word in self.used_words

    def __repr__(self):
        return f'{self.user_name} {self.used_words}'