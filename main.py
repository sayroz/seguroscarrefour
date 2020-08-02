#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Esse programa é destinado apenas para fins didádicos.

"""
Um Bot simples que simula a cotação de seguros de veículos do Banco Carrefour.
O bot utiliza classes da biblioteca python-telegram-bot para envio e manipulação de mensagens do telegram.

Primeiro, algumas funções do manipulador são definidas. Em seguida, essas funções são passadas para
expedidor e registrado em seus respectivos locais.
Em seguida, o bot é iniciado e executado até pressionar Ctrl-C na linha de comando.
Uso:pi
Basicamente o bot direciona o usuário para os valores de acordo com o que deseja.
Pressiona Ctrl-C para finalizar o processo do BOT.
"""
#framework web
from flask import Flask
app = Flask(__name__)
import telegram, json
from Conf.settings import TELEGRAM_TOKEN,EUROP_ASSISTANCE, REALIZA_ASSISTANCE
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

# Enable logging: Coleta Infos do usuário no Telegram
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

#Iniciando a iteração com o comando /start
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    site = 'Bem vindo ao Bot Carrefour Seguros'
    main()
    return site

def start(update, context):
    #Limita as opções de escolha para o usuário
    reply_keyboard = [['Carro', 'Moto']]

    #Primeira iteração
    update.message.reply_text(
        'Olá! Meu nome é Sofia. Bem vindo(a) ao <b>SegurosCarrefour!</b>\n\n'
        'Vamos fechar um seguro para o seu veículo hoje?  '
        'Escolha veículo deseja realizar a cotação....\n\n'
        '<i>Caso queira sair da conversa, digite <a>/cancelar</a></i>',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        parse_mode=telegram.ParseMode.HTML)

# 2° Iteração: O usuário envia o tipo de veículo que quer o seguro
def veiculo(update, context):
    #Coleta a mensagem do usuario
    Veiculo = update.message.text

    #Salva a infomação para uso externo
    context.user_data['veiculo'] = Veiculo

    #Se usuário escolher Moto, pergunte quantas cilindradas tem o veículo
    if Veiculo == 'Moto':
        reply_keyboard = [['Até 125 Cilindradas', 'De 126 a 250 Cilindradas']]
        update.message.reply_text('Sua <b>'+Veiculo+'</b> possui quantas cilindradas?',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
                                  parse_mode=telegram.ParseMode.HTML)
    else:
        reply_keyboard = [['2020', '2019', '2018','2017','2016','2015']]
        update.message.reply_text(
            'Maravilha! Por favor, informe o ano de fabricação do seu <b>'+Veiculo+'</b>',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
                parse_mode=telegram.ParseMode.HTML)

#3° Iteração Condicional: Caso o usuário escolheu moto, salva as cilindradas e pergunta o ano do veículo
def moto(update, context):
    # Salvando as cilindradas para uso externo
    Cilindradas = update.message.text
    context.user_data['cilindradas'] = Cilindradas

    #Retorna o veículo escolhido na função anterior
    Veiculo = context.user_data['veiculo']

    #Solicita o ano de fabricação ao usuário
    reply_keyboard = [['2020', '2019', '2018', '2017', '2016', '2015']]
    update.message.reply_text('Maravilha...! Por favor, me informe o ano de fabricação da sua <b>'+ Veiculo+'</b>',
                                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
                                parse_mode=telegram.ParseMode.HTML)

#4° Iteração, coleta os dados informados, exporta  para arquivo JSON e envia as opções de compra
def Opcoes(update, context):
    # Salvando o ano do veículo para uso externo
    AnoVeiculo = update.message.text
    context.user_data['ano'] = AnoVeiculo

    # Retorna o usuário loggado no telegram
    user = update.message.from_user
    #Retorna a Variavel Veículo
    Veiculo = context.user_data['veiculo']

    #Envia opções de seguros ao usuário
    if Veiculo == 'moto':
        msg = 'temos as seguintes opções para o seu'
    else:
        msg = 'temos as seguintes opções para a sua'

    update.message.reply_text(
        'Muito bem Sr(a). <b>'+user.first_name+'</b>,'+msg+' '
        '<b>'+Veiculo+'</b>, ano <b>'+AnoVeiculo+'</b>:',parse_mode=telegram.ParseMode.HTML)


    #Nesse trecho deveríamos  personalizar os valores de acordo com o filtro do usuário
    #Se veiculo = Carro, Busca tabela carro, onde ano = AnoVeiculo  select preços e condições
    #Senão busca tabela Moto,  onde cilindradas = cilindradas e ano = Anoveiculo, select preços e condições
    # Porém, ficará para próxima versão do programa.

    update.message.reply_text('<b>Opção 1:</b> Realiza Assistência',parse_mode=telegram.ParseMode.HTML)
    update.message.reply_photo(REALIZA_ASSISTANCE)
    update.message.reply_text('<b>Opção 2:</b> Europ Assistance',parse_mode=telegram.ParseMode.HTML)
    update.message.reply_photo(EUROP_ASSISTANCE)
    # Fim do trecho resultados de cotações

    #Pergunta ao usuário qual opção lhe agrada
    reply_keyboard = [['Opção 1: Realiza Assistance', 'Opção 2: Europ Assistance']]
    update.message.reply_text(' Escolha a operadora para finalizar a aquisição do seguro:',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

def operadora(update, context):
    # Coleta a mensagem do usuario
    Operadora = update.message.text

    # Salva a infomação para uso externo
    key = 'operadora'
    context.user_data[key] = Operadora
    #Mensagem Finaliza
    update.message.reply_text('Parabéns! Fez uma excelente escolha')
    Exportar()


#Iteração Auxiliar: O cliente deseja cancelar
def cancelar(update, context):
    user = update.message.from_user
    update.message.reply_text('Até Mais! No que precisar, estou à disposição.',
                              reply_markup=ReplyKeyboardRemove())
def Exportar():
    # Exportanto JSON
    Cotacao = []
    # Retorna os dados escolhidos nas iterações anteriores
    user = update.message.from_user
    Veiculo = context.user_data['veiculo']
    Ano = context.user_data['ano']
    if Veiculo == "Moto":
        Cilindradas = context.user_data['moto']
    else:
        Cilindradas = 0
    Operadora = context.user_data['operadora']

    Cotacao.append({'User': user, 'Veiculo': veiculo, 'Ano': Ano,
                    'Cilindradas': Cilindradas, 'Operadora': Operadora})

    with open('cotacoes.json', 'w') as json_file:
        json.dump(Cotacao, json_file, indent=3, ensure_ascii=False)

    # Salvando os dados em arquivo JSON

def main():
    #ABAIXO, COMENTÁRIOS DO PACOTE PYTHON-TELEGRAM-BOT
    """Start the bot. """
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler('cancelar', cancelar))
    dp.add_handler(MessageHandler(Filters.regex('^(Carro|Moto)$'), veiculo))
    dp.add_handler(MessageHandler(Filters.regex('^(Até 125 Cilindradas|De 126 a 250 Cilindradas)$'), moto))
    dp.add_handler(MessageHandler(Filters.regex('^(2020|2019|2018|2017|2016|2015 ou anterior)$'), Opcoes))
    dp.add_handler(MessageHandler(Filters.regex('^(Opção 1: Realiza Assistance|Opção 2: Europ Assistance)$'), operadora))


    # Start the Bot
    updater.start_polling()


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()




if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)