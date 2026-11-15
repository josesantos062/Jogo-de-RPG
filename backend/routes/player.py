from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/player')



def player():
    atribucts_player = {
        'attack_player': 10,
        'defense_player': 10,
        'hp_player': 10
    }

    return jsonify(atribucts_player)



if __name__ == '__main__':
    app.run(debug=True)