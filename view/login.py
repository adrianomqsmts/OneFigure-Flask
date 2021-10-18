import requests


def loginview(name, password):
    isvalid, user, figure = _login(name, password)
    if isvalid:
        print('Bem-vindo {}'.format(user['name']))
        if user['showcard']:
            print('\n ------------ Figurinha Adquirida no Sorteio díario ------------------')
            print("ID | NOME | RARIDADE | ")
            print(figure['idFigure'], '|', figure['name'], '|', figure['rarity'], '\n')
        return user, isvalid, figure
    else:
        print('Nome e/ou senha inválidos')
        return None, None, None


def _login(name, password):
    r = requests.post('http://localhost:5000/', data={'name': name, 'password': password})
    response = r.json()
    isvalid = response['response']
    user = response['user']
    figure = response['figure']

    return isvalid, user, figure
