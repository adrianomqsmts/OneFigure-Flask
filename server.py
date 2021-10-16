import flask
from flask import request, jsonify
from model import user
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    database = user.login(name=name, password=password)

    if database:
        usuario = {
            'idUser': int(database[0]['idUser']),
            'name': database[0]['name'],
            'balance': float(database[3]),
            'password': database[0]['password'],
            'showcard': int(database[2]['showcard']),
        }

        if int(database[2]['showcard']):
            figure = {
                'idFigure': database[1]['idFigure'],
                'rarity': database[1]['rarity'],
                'name': database[1]['name'],
                'path': database[1]['path']
            }
        else:
            figure = None

        out = {'response': True, 'user': usuario, 'figure': figure}
    else:
        out = {'response': False, 'user': None, 'figure': None}

    return jsonify(out)

app.run()

