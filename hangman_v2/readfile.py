from random import randint

class ReadFile():
  def __init__(self):
    with open('words.txt', 'rt') as file:
      self.__words = file.readlines()
  
  def getword(self):
    return self.__words[randint(0, len(self.__words))].strip()