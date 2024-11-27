class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    
    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                all_words[file.name] = []
                for line in file:
                    for x in ',', '.', '=', '!', '?', ';', ':', ' - ':
                        line = line.replace(x, ' ')
                    all_words[file.name] += line.lower().strip().split()
        return all_words
    
    def find(self, word):
        result = dict()
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result
    
    def count(self, word):
        result = dict()
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.count(word)
        return result


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
