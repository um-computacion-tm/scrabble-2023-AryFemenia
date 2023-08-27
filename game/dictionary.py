class Dictionary:
    def __init__(self):
        #make a list with all the words starting with the letter 'A' from the spanish dictionary
        self.words = []
        with open('game/dictionary.txt') as file:
            for line in file:
                if line[0] == 'A':
                    self.words.append(line.strip())

    def check(self, word):
        return word in self.words