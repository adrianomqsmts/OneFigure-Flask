import flask
from flask import request, jsonify
from model import user, album as al, figura as figure

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


@app.route('/create', methods=['POST'])
def create():
    name = request.form.get('name')
    password = request.form.get('password')
    database = user.create(name=name, password=password)
    if database:
        result = {
            'response': True,
        }
    else:
        result = {
            'response': False,
        }
    return jsonify(result)


@app.route('/album', methods=['POST'])
def album():
    id = request.form.get('idUser')
    database = al.show(id_user=id)
    if database:
        complete = int(database[1]['complete'])
        if complete:
            special = {
                'idFigure': database[2]['idFigure'],
                'rarity': database[2]['rarity'],
                'name': database[2]['name'],
                'path': database[2]['path']
            }
        else:
            special = None
        figures = []
        newdata = sorted(database[0], key=lambda k: k['idFigure'])
        for data in newdata:
            figures.append({
                'idFigure': data['idFigure'],
                'name': data['name'],
                'rarity': data['rarity'],
                'path': data['path'],
                'quantity': data['quantity']
            })
        out = {
            'response': True,
            'complete': complete,
            'special': special,
            'figures': figures,
        }
    else:
        out = {
            'response': False,
            'complete': 0,
            'special': None,
            'figures': None,
        }
    return jsonify(out)


@app.route('/buy', methods=['POST'])
def buy():
    idUser = request.form.get('idUser')
    database = figure.buy(idUser)
    result = []
    if database:
        balance = float(database[3])
        del database[3]
        for i in range(3):
            result.append({
                'idFigure': database[i]['idFigure'],
                'rarity': database[i]['rarity'],
                'name': database[i]['name'],
                'path': database[i]['path']
            })
        figures = result
        out = {
            'response': True,
            'balance': balance,
            'figures': figures,
        }
    else:
        out = {
            'response': False,
            'balance': None,
            'figures': None,
        }
    return jsonify(out)


@app.route('/trade/create', methods=['POST'])
def createTrade():
    idUser = request.form.get('idUser')
    offer = request.form.get('offer')
    taking = request.form.get('taking')
    if (int(offer) >= 0) and (int(taking) >= 0) and (int(offer) <= 50) and (int(taking) <= 50):
        database = figure.createTrade(idUser=idUser, offer=offer, taking=taking)
        if database:
            out = {
                'response': True,
            }
        else:
            out = {
                'response': False,
            }
    else:
        out = {
            'response': False,
        }

    return jsonify(out)


@app.route('/trade/list', methods=['GET'])
def listTrade():
    database = figure.listTrade()
    if database:
        result = []
        for data in database:
            result.append({
                'name': data['name'],
                'idTrade': data['idTrade'],
                'offerID': data['offerID'],
                'offerName': data['offerName'],
                'offerRarity': data['offerRarity'],
                'takingID': data['takingID'],
                'takingName': data['takingName'],
                'takingRarity': data['takingRarity']
            })
        out = {
            'response': True,
            'list': result
        }
    else:
        out = {
            'response': False,
            'list': None
        }
    return jsonify(out)


@app.route('/sell', methods=['POST'])
def sell():
    idUser = request.form.get('idUser')
    idFigure = request.form.get('idFigure')
    database = figure.sell(idUser, idFigure)
    if database:
        name = database['name']
        price = float(database['price'])
        out = {
            'response': True,
            'price': price,
            'name': name
        }
    else:
        out = {
            'response': False,
            'price': None,
            'name': None
        }
    return jsonify(out)


@app.route('/trade/trade', methods=['POST'])
def Trade():
    idUser = request.form.get('idUser')
    idTrade = request.form.get('idTrade')
    database = figure.trade(idUser, idTrade)
    if database:
        out = {
            'response': True
        }
    else:
        out = {
            'response': False
        }
    return jsonify(out)

app.run()

