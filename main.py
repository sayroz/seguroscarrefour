#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Esse programa é destinado apenas para fins didádicos.

"""
Um Bot simples que simula a cotação de seguros de veículos do Banco Carrefour.
O bot utiliza classes da biblioteca python-telegram-bot para envio e manipulação de mensagens do telegram.

Primeiro, algumas funções do manipulador são definidas. Em seguida, essas funções são passadas para
expeditor e registrado em seus respectivos locais.
Em seguida, o bot é iniciado e executado até pressionar Ctrl-C na linha de comando.
Uso:pi
Basicamente o bot direciona o usuário para os valores de acordo com o que deseja.
Pressiona Ctrl-C para finalizar o processo do BOT.
"""
#framework para rodar o bot na nuvem
from flask import Flask

#importando as funções com iterações do bot
import functions

#identifica para o framework o app
app = Flask(__name__)

@app.route('/')
def BotCarrefour():
    #mensagem para pagina web
    functions.main()
    nuvem = 'Estamos online procure @seguroscarrefour no telegram'
    return nuvem

if __name__ == '__main__':
    #functions.main()
    app.run(host='127.0.0.1', port=8080, debug=True)