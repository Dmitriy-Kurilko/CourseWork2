class BasicWord:
    def __init__(self, main_word, acceptable_list):
        self.main_word = main_word
        self.acceptable_list = acceptable_list

    def search_bool(self):
        for i in self.acceptable_list:
            if i in self.main_word:
                return True
        return False

    def counter_len_acceptable_list(self):
        return len(self.acceptable_list)

    def __repr__(self):
        return f'{self.main_word} {self.acceptable_list}'
