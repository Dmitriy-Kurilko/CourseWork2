class BasicWord:
    def __init__(self, word, list_with_words):
        self.word = word
        self.list_with_words = list_with_words

    def checker(self, user_answer):
        return user_answer in self.list_with_words

    def len_of_list(self):
        return len(self.list_with_words)

    def __repr__(self):
        return f'{self.word}: {self.list_with_words}'

