import readfile
import board
import os

class Hangman():
    def __init__(self, word):
        self.__word = word
        self.__right_letter = []
        self.__wrong_letter = []

    def get_word(self):
        return self.__word

    def guess(self, letter):
        if letter in self.__word and letter not in self.__right_letter:
            self.__right_letter.append(letter) 
        elif letter not in self.__word and letter not in self.__wrong_letter:
            self.__wrong_letter.append(letter)
        else:
            return False
        return True

    def game_over(self):
        return self.game_won() or len(self.__wrong_letter) == 6

    def game_won(self):
        if '_' not in self.hide_word():
            return True
        return False
    
    def hide_word(self):
        result = ''
        for letter in self.__word:
            if letter not in self.__right_letter:
                result += '_ '
            else:
                result += letter
        return result

    def game_status(self, board):
        self.clear()
        print(board[len(self.__wrong_letter)])
        print("\nWord: " + self.hide_word())
        print("\nWrong words:")
        for i in self.__wrong_letter:
            print(i)
        print("\nRigth words:")
        for i in self.__right_letter:
            print(i)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(">>>>>>>>>>>>>>>Hangman<<<<<<<<<<<<<<<")

def main():
    game = Hangman(readfile.ReadFile().getword())
    game_board = board.Board()
    
    while not game.game_over():
        game.game_status(game_board)
        letter = input("\nInput a letter: ")
        game.guess(letter)

    game.game_status(game_board)

    if game.game_won():
        print("\nCongratulations! You won!")
    else:
        print("Game over! The right word is " + game.get_word())

if __name__ == "__main__":
    main()