import file

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

def main()
    
word = file.ReadFile()
print(word)

board = [
'''
  +---+
      |
      |
      |
      |
      | 
============= ''',
'''
  +---+
  0   |
      |
      |
      |
      | 
============= ''',
'''
  +---+
  0   |
  |   |
      |
      |
      | 
============= ''',
'''
  +---+
  0   |
 /|   |
      |
      |
      | 
============= ''',
'''
  +---+
  0   |
 /|\  |
      |
      |
      | 
============= ''',
'''
  +---+
  0   |
 /|\  |
 /    |
      |
      | 
============= ''',
'''
  +---+
  0   |
 /|\  |
 / \  |
      |
      | 
============= ''']

for i in board:
    print(i)
