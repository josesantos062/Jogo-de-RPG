from flask import Flask, jsonify

app = Flask(__name__)
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