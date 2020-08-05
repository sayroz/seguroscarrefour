# Enable logging: Coleta Infos do usuário no Telegram
import logging
import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
from Conf.settings import TELEGRAM_TOKEN
from SegurosBKP import veiculos
from SegurosBKP import pets


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


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

    dp.add_handler(MessageHandler(Filters.regex('^(1|2|3|4|5|6)$'), opSeguro))
    dp.add_handler(MessageHandler(Filters.regex('^(Carro|Moto)$'), veiculos.veiculo))
    dp.add_handler(MessageHandler(Filters.regex('^(Cachorro|Gato)$'), pets.pets))
    dp.add_handler(MessageHandler(Filters.regex('^(1 ano|2 anos|3 anos|4 anos|5 anos|6 anos|7 anos)$'), pets.OpcoesPets))
    dp.add_handler(MessageHandler(Filters.regex('^(Até 125 Cilindradas|De 126 a 250 Cilindradas)$'), veiculos.moto))
    dp.add_handler(MessageHandler(Filters.regex('^(2020|2019|2018|2017|2016|2015)$'), veiculos.OpcoesVeiculo))
    dp.add_handler(MessageHandler(Filters.regex('^(Opção 1: Realiza Assistance|Opção 2: Europ Assistance)$'), veiculos.operadora))
    dp.add_handler(MessageHandler(Filters.regex('^(Opção 1: AmigoO)$'), pets.operadoraPet))


    # Start the Bot
    updater.start_polling()


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def start(update, context):
    #Limita as opções de escolha para o usuário
    reply_keyboard = [['1','2','3','4','5','6','7']]
    #Primeira iteração
    update.message.reply_text(
        'Olá! Meu nome é Sofia. Bem vindo(a) ao <b>SegurosCarrefour!</b>\n\n'
        'Previna-se e cuide do que mais importa. Qual seguro pretende fechar hoje?\n\n'
        '<b>1</b> - Auto e Motos \n'
        '<b>2</b> - Pets \n'
        '<b>3</b> - Residencial \n'
        '<b>4</b> - Acidentes Pessoais \n'
        '<b>5</b> - Viagem \n'
        '<b>6</b> - Celular \n\n'
        '<i>Caso queira voltar ao início, digite <a>/START</a></i>',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        parse_mode=telegram.ParseMode.HTML)


#Iteração Auxiliar: O cliente deseja cancelar
def cancelar(update, context):
    user = update.message.from_user
    update.message.reply_text('Até Mais! No que precisar, estou à disposição. '
                              'Caso queira uma nova cotação, aperte:  <b><a>/START</a></b>',
                              reply_markup=ReplyKeyboardRemove(),parse_mode=telegram.ParseMode.HTML)

def opSeguro(update, context):
    op = update.message.text
    if op == '1':
        reply_keyboard = [['Carro', 'Moto']]
        update.message.reply_text('Certo, deseja orçar <b>Carro</b> ou <b>Moto</b>?',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
                                  parse_mode=telegram.ParseMode.HTML)
    elif op == '2':
        reply_keyboard = [['Cachorro', 'Gato']]
        update.message.reply_text('Muito bem, deseja falar sobre <b>Cachorro</b> ou <b>gato</b>?',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
                                  parse_mode=telegram.ParseMode.HTML)
    else:
        reply_keyboard = [['1','2','3','4','5','6','7']]
        update.message.reply_text('Ops!  Ainda não aprendi a cotar este seguro.\n'
                                  ' Tente <b> 1 - Veículos/Motos</b> ou <b>2 - Pets!</b> ;)',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
                                  parse_mode=telegram.ParseMode.HTML)


if __name__ == '__main__':
    main()

    # Salvando os dados em arquivo JSON
# Iniciando a iteração com o comando /start


