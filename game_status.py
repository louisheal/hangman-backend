from enum import Enum


class GameStatus(Enum):
  NEW_GAME = 1
  CORRECT_GUESS = 2
  INCORRECT_GUESS = 3
  GAME_WON = 4
  GAME_LOST = 5
  REPEATED_GUESS = 6


status_messages = {
  GameStatus.NEW_GAME: None,
  GameStatus.CORRECT_GUESS: "Correct guess!",
  GameStatus.INCORRECT_GUESS: "Incorrect guess!",
  GameStatus.GAME_WON: "Congratulations, you won!",
  GameStatus.GAME_LOST: "Nooo! You lost!",
  GameStatus.REPEATED_GUESS: "You have already guessed that letter!"
}


def game_over(status: GameStatus) -> bool:
  return status in [GameStatus.GAME_WON, GameStatus.GAME_LOST]
