from enum import Enum

class GameStatus(Enum):
  NEW_GAME = 1
  CORRECT_GUESS = 2
  INCORRECT_GUESS = 3
  GAME_WON = 4
  GAME_LOST = 5
  REPEATED_GUESS = 6
