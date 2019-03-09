#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api
from connection import *
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    hist = buscahistorico()
    return render_template(
        'weather.html',
        hist=hist)


@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('input_field')
    inserirhistorico(select)
    resp = query_api(select)

    pp(resp)
    if resp:
        data.append(resp)

    # if len(data) != 2:

    return render_template('result.html', data=data, error=error)


def buscahistorico():
    con = Conexao('localhost', 'weather', 'postgres', 'admin')
    rs = con.consultar("""SELECT descricao as desc FROM weather.consulta_hist ORDER BY ID desc LIMIT 4""")
    # pp(rs)
    # for linha in rs:
    #     pp(linha)
    return rs


def inserirhistorico(valor):
    con = Conexao('localhost', 'weather', 'postgres', 'admin')
    pk = con.proximaPK('weather.consulta_hist', 'id')

    sql = "INSERT INTO weather.consulta_hist(id, descricao) VALUES ({},{})"
    pp(sql.format(pk, valor))
    con.manipular(sql.format(pk, valor))


if __name__ == '__main__':
    app.run(debug=True)




