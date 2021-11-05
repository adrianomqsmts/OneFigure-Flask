# OneFigure - Flask

Trabalho prático da disciplina de Sistemas Distribuídos e Paralelos da 🏫 Universidade Federal de Viçosa - Campus Florestal. 

Este trabalho teve como objetivo desenvolver um sistema de figurinhas de nossa escolha, neste caso do anime One Piece, usando o web service Python REST para comunicar entre o Cliente e o Servidor como uma API. 

Dentre as funcionalidades do sistema temos:

- Criar e entrar na conta
- Sorteio de figurinhas pelo login diário
- Comprar, vender e visualizar figurinhas
- Anunciar, ver e trocar figurinhas

### 💻 Interface 

Abaixo temos um exemplo de umas das telas do sistema, onde o usuário ganhou figurinhas através da compra. 

![](readme/interface.png)


********************************************


## 🚀 Começando

O sistema foi desenvolvido em um único projeto, juntando o cliente e o servidor, de tal modo que para que seja executado, deve levar em consideração os diferentes arquivos. 

Para obter uma cópia deste projeto:

```shell
git clone https://github.com/adrianomqsmts/OneFigure-REST
cd exemplo
```

Para iniciar o servidor:

```shell
 python server.py
```

Para iniciar o Cliente padrão pelo terminal:

```shell
 python client.py
```

Para iniciar o Cliente com interface Gráfica:

```shell
 python client-interface.py
```

### 📋 Pré-requisitos

As bibliotecas usadas neste projeto podem ser encontradas no arquivo "requirements.txt"

```shell
pip install -r requirements.txt 
```

## 🛠️ Construído com

Ferramentas, linguagens e outras tecnologias usadas no desenvolvimento deste sistema.

* [PyCharm](https://www.jetbrains.com/pycharm/) - Ambiente de Desenvolvimento
* [Git](https://git-scm.com/) - Controle de Versões
* [SQLite](https://www.sqlite.org/docs.html) - Banco de Dados
* [TKinter](https://docs.python.org/3/library/tkinter.html) - Biblioteca de Interface Python
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Micro framework de Desenvolvimento
* [requests](https://docs.python-requests.org/en/latest/) - Biblioteca de requisições HTTP 

## ✒️ Autores

* **Desenvolvedor** - *Código e Documentação* - [Adriano](https://github.com/adrianomqsmts)
* **Desenvolvedor** - *Código e Documentação* - [Eduardo](https://github.com/eduardovbe)

## 📄 Licença

Este projeto está sob a licença MIT License - veja o arquivo [LICENSE.md](https://github.com/adrianomqsmts/OneFigure-Flask/blob/master/LICENSE) para detalhes.

---
