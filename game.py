from game_status import GameStatus

# TODO: Move to config
START_LIVES = 6

class Game:
  def __init__(self, word) -> None:
    self.__lives = START_LIVES
    self.__guessed_letters = []
    self.__word = word
    self.__status = GameStatus.NEW_GAME

  def make_guess(self, letter) -> GameStatus:
    if letter in self.__guessed_letters:
      self.__status = GameStatus.REPEATED_GUESS
      return
    
    self.__guessed_letters.append(letter)
    if letter not in self.__word:
      self.__lives -= 1
      self.__status = GameStatus.INCORRECT_GUESS
      return

    if self.__lives <= 0:
      self.__status = GameStatus.GAME_LOST
      return
    
    for letter in self.__word:
      if letter.isalpha() and letter not in self.__guessed_letters:
        self.__status = GameStatus.CORRECT_GUESS
        return
    
    self.__status = GameStatus.GAME_WON
  
  def get_word(self) -> str:
    guessed_word = ""
    for letter in self.__word:
      if letter.isalpha() and letter not in self.__guessed_letters:
        guessed_word += '_'
      elif letter == ' ':
        guessed_word += '\n'
      else:
        guessed_word += letter
      guessed_word += ' '
    return guessed_word[:-1]
  
  def get_lives(self) -> int:
    return self.__lives
  
  def get_status(self) -> GameStatus:
    return self.__status
