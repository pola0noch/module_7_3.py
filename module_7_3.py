# Домашнее задание по теме "Оператор "with".

import string
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                content = file.read().lower()
                translator = str.maketrans("", "", string.punctuation.replace('-', ''))
                cleaned_content = content.translate(translator)
                words = cleaned_content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                result[file_name] = position
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
















