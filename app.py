from flask import Flask, request
from flask_cors import CORS

from game import Game
from game_status import GameStatus

app = Flask(__name__)
cors = CORS(app)

# TODO: Store game in MongoDB
game = Game("JAZZ")

@app.route('/new_game/<string:word>')
def new_game(word):
  global game
  game = Game(word)
  return 200

@app.route('/guess', methods=['POST'])
def guess():
  global game
  letter = request.form['letter']

  # TODO: Make error message class / enums
  if game.get_status() in [GameStatus.GAME_WON, GameStatus.GAME_LOST]:
    return "", 400
  if not letter.isalpha() or len(letter) != 1:
    return "", 400
  
  game.make_guess(letter.upper())
  return "", 200

@app.route('/status')
def get_state():
  global game
  return {'word': game.get_word(), 'status': game.get_status().value}

if __name__ == '__main__':
  app.run(debug=True)
