
import os
from flask import Flask
from cs50 import SQL

db = SQL("sqlite:///../db/paipj.db")

app = Flask(__name__)

@app.route("/")
def hello():
    # Return all results of query
    lista = db.execute('SELECT * FROM pacientes')
    return f'Olá {lista[0]["nome"]}'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=os.environ['PORT'])