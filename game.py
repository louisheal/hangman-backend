from game_status import GameStatus, game_over


# TODO: Move to config
START_LIVES = 6


class Game:
  def __init__(self, word: str) -> None:
    self.__lives = START_LIVES
    self.__guessed_letters = []
    self.__word = word
    self.__status = GameStatus.NEW_GAME

  # TODO: Move data validation to frontend
  def make_guess(self, letter: str) -> None:
    if letter.isalpha() and len(letter) == 1 and not game_over(self.__status):
      self.__status = self.__update_game(letter)

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

  def __update_game(self, letter: str) -> GameStatus:
    if letter in self.__guessed_letters:
      return GameStatus.REPEATED_GUESS
    self.__guessed_letters.append(letter)
    if letter not in self.__word:
      self.__lives -= 1
      return GameStatus.INCORRECT_GUESS
    if self.__lives <= 0:
      return GameStatus.GAME_LOST
    for letter in self.__word:
      if letter.isalpha() and letter not in self.__guessed_letters:
        return GameStatus.CORRECT_GUESS
    return GameStatus.GAME_WON
