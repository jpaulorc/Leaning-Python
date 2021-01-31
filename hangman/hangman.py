import file
import board

class Hangman():
    def __init__(self, word):
        pass
    def guess(self, letter):
        pass
    def gameover(self):
        pass
    def gamewon(self):
        pass
    def hide_word(self):
        pass
    def status(self):
        pass

def main():
    hangman = Hangman()

word = file.ReadFile()
print(word)
b = board.Board()
print(b[0])
print(b.len())
