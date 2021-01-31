import file
import board
import os

class Hangman():
    def __init__(self, word):
        print(">>>>>>>>>>>>>>>Hangman<<<<<<<<<<<<<<<")
        self__word = word
    
    # Método para adivinhar a letra
    def guess(self, letter):
        letter = input("Input a letter: ")
        if letter in self__word:
            return True
        return False

    # Método para verificar se o jogo terminou
    def gameover(self):
        pass

    # Método para verificar se o jogador venceu
    def gamewon(self):
        pass

    # Método para não mostrar a letra no board
    def hide_word(self):
        pass

    # Método para checar o status do game e imprimir o board na tela
    def status(self):
        pass

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    game = Hangman(file.ReadFile())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    game_board = board.Board()
    for i in range(game_board.len()):
        game.clear()
        print(game_board[i])
    else:
        print("teste")

	# Verifica o status do jogo
    game.status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.gamewon():
        print("\nCongratulations! You won!")
    else:
        print("\nGame over!")

if __name__ == "__main__":
    main()