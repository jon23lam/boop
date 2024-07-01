from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from backend.models.Player import Player
from backend.models.Board import Board

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

# Initialize the game
player1 = Player(1)
player2 = Player(2)
game_board = Board(player1, player2)


@app.route('/make_move', methods=['POST'])
@cross_origin(supports_credentials=True)
def make_move():
    data = request.get_json()
    player_piece = data['player_piece']
    row = data['row']
    col = data['col']

    if player_piece == 'x' or player_piece == 'o':
      game_board.current_turn.active_kittens += 1
    else:
      game_board.current_turn.active_cats += 1
      
    game_board.make_move(player_piece, row, col)
    
    winner = game_board.check_win_or_upgrade()

    if winner != None:
       winner = winner.player
    return jsonify({'board': game_board.board, 'winner': winner})


@app.route('/game_state', methods=['GET'])
@cross_origin(supports_credentials=True)
def game_state():
    return jsonify({
        'board': game_board.board, 
        'currentTurn': game_board.current_turn.player,
        "numKittens": game_board.current_turn.kittens - game_board.current_turn.active_kittens,
        "numCats": game_board.current_turn.cats - game_board.current_turn.active_cats
      })

@app.route('/reset', methods=['POST'])
@cross_origin(supports_credentials=True)
def reset():
    del player1
    del player2
    del game_board
    player1 = Player(1)
    player2 = Player(2)
    game_board = Board(player1, player2)
    return jsonify({'board': game_board.board, 'currentTurn': game_board.current_turn.player})

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, jsonify
# from flask_cors import CORS, cross_origin

# app = Flask(__name__)
# CORS(app, support_credentials=True)

# @app.route("/login")
# @cross_origin(supports_credentials=True)
# def login():
#   return jsonify({'success': 'ok'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
