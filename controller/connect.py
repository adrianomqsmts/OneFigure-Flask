def connect():
    import sqlite3
    conn = sqlite3.connect('oneFigure.db')
    return conn
