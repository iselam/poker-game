from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from Database import session, new_game

app = Flask(__name__)
CORS(app)

players = []

# players to play
@app.route('/api/players-to-play', methods=['POST'])
def players_to_play():
    data = request.get_json()

    if not all(key in data for key in ["player_one","player_two","player_three","player_four"]):
        return jsonify({"error":"Faltan datos en el JSON"}), 400

    players = new_game(data)

    return players, 200

if __name__ == '__main__':
    app.run(debug=True)