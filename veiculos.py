import telegram
from Conf.settings import EUROP_ASSISTANCE, REALIZA_ASSISTANCE
from telegram import ReplyKeyboardMarkup


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
def OpcoesVeiculo(update, context):
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


    # Exportanto JSON
    #Cotacao = []
    # Retorna os dados escolhidos nas iterações anteriores
    #user = message.from_user
    #Veiculo = context.user_data['veiculo']
    #Ano = context.user_data['ano']
    #if Veiculo == "Moto":
    #    Cilindradas = context.user_data['moto']
    #else:
     #   Cilindradas = 0
   # Operadora = veiculos.context.user_data['operadora']

   # Cotacao.append({'User': user, 'Veiculo': Veiculo, 'Ano': Ano,
       #             'Cilindradas': Cilindradas, 'Operadora': Operadora})

   # with open('cotacoes.json', 'w') as json_file:
      #  json.dump(Cotacao, json_file, indent=3, ensure_ascii=False)