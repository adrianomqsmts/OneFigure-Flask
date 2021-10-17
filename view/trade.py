import requests


def tradeview(user, idTrade):
    response = _trade(user['idUser'], idTrade)
    if response:
       print('A troca ocorreu com sucesso')
    else:
        print('Lamentamos, mas não foi possível finalizar a troca, verifique suas cartas')


def _trade(idUser, idTrade):
    r = requests.post(
        'http://localhost:5000/trade/trade',
        data={'idUser': idUser, 'idTrade': idTrade}
    )
    response = r.json()
    isvalid = response['response']

    return isvalid

