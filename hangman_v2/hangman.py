import file
import board
import os

class Hangman():
    def __init__(self, word):
        self.__word = word
        self.__right_letter = []
        self.__wrong_letter = []
        self.__hide_word = []
        self.__move = 0
    
    def gethideword(self):
        self.__hide_word = ['_' for i in self.__word]
        return ' '.join(self.__hide_word)

    def getrightandwrongletters(self):
        return self.__right_letter, self.__wrong_letter

    def guess(self, letter):
        if letter in self.__word:
            self.__right_letter.append(letter) 
            return 0
        else:
            self.__wrong_letter.append(letter)
            return 1

    def gameover(self, move, board):
        if (move + 1 == board.len()) and (self.__word != ''.join(self.__hide_word)):
            return True
        return False

    def gamewon(self):
        if self.__word == ''.join(self.__hide_word):
            return True
        return False

    def hide_word(self, letter):
        for i in range(len(self.__word)):
            if self.__word[i] == letter:
                self.__hide_word[i] = letter
        
        return ' '.join(self.__hide_word)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(">>>>>>>>>>>>>>>Hangman<<<<<<<<<<<<<<<")

def main():
    game = Hangman(file.ReadFile().getword())
    game.clear()
    
    game_board = board.Board()
    hide_word = game.gethideword()
    right_letter, wrong_letter = [], []

    move = 0
    while True:
        game.clear()
        print(game_board[move])
        print('Word: ' + hide_word)
        
        print("\nRight Letters:")
        print_letters(right_letter)

        print("\nWrong Letters:")
        print_letters(wrong_letter)
        
        if game.gamewon():
            print("\nCongratulations! You won!")
            break
        if game.gameover(move, game_board):
            print("\nGame over!")
            break

        letter = input("\nInput a letter: ")
        hide_word = game.hide_word(letter)
        move += game.guess(letter)
        right_letter, wrong_letter = game.getrightandwrongletters()

def print_letters(letters):
    if len(letters) > 0:
        for i in letters:
            print(i)

if __name__ == "__main__":
    main()