import requests


def singinview(name, password):
    response = _singin(name, password)
    if response:
        print('Conta criada com sucesso.')
    else:
        print('Não foi possível criar a conta, possívelmente o nome já existe')


def _singin(name, password):
    r = requests.post('http://localhost:5000/create', data={'name': name, 'password': password})
    response = r.json()
    isvalid = response['response']

    return isvalid
