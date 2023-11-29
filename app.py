from flask import Flask, request
from flask_cors import CORS


from game import Game
import game_status as gs


app = Flask(__name__)
cors = CORS(app)


# TODO: Use dict of games
game = Game("JAZZ")


@app.route('/new_game/<string:word>')
def new_game(word):
  global game
  game = Game(word.upper())
  return "", 200


# TODO: Better return message
@app.route('/guess', methods=['POST'])
def guess():
  letter = request.form['letter']
  game.make_guess(letter.upper())
  return "", 200


@app.route('/status', methods=["GET"])
def get_status():
  status = game.get_status()
  return {
    'word': game.get_word(),
    'msg': gs.status_messages.get(status),
    'lives': game.get_lives(),
    'done': gs.game_over(status)
    }


if __name__ == '__main__':
  app.run(debug=True)
