'''
IN DEVELOOPMENT
file_path = "starting_letter/a.txt"

class Dictionary:
    def __init__(self):
        self.words = []
        with open('starting_letter/a.txt') as file:
            for line in file:
                if line[0] == 'A':
                    self.words.append(line.strip())

    def check(self, word):
        return word in self.words

file_path = "game/starting_letter/a.txt"

try:
    with open(file_path, "a") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
'''