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
    game = Hangman(file.ReadFile())
    game.status()
    if game.gamewon():
        print("\nCongratulations! You won!")
    else:
        print("\nGame over!")

if __name__ == "__main__":
    main()
