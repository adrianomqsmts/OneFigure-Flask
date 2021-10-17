import requests


def albumview(user):

    isvalid, complete, special, figures = _album(user)

    if isvalid:
        print('\n ------------ ALBUM ------------------')
        print("ID | NOME | RARIDADE | QUANTIDADE")
        for figure in figures:
            print(figure['idFigure'], '|', figure['name'], '|', figure['rarity'], '|', figure['quantity'])
        if complete == 1:
            print('\nParabéns você completou o album e ganhou uma figurinha ESPECIAL exclusiva:\n')
            print("ID | NOME | RARIDADE")
            print(special['idFigure'], '|', special['name'], '|', special['rarity'])
        print()

    else:
        print('Lamentamos, mas não foi possível encontrar o álbum')


def _album(user):
    r = requests.post('http://localhost:5000/album', data={'idUser': user['idUser']})
    response = r.json()
    isvalid = response['response']
    complete = response['complete']
    special = response['special']
    figures = response['figures']

    return isvalid, complete, special, figures


