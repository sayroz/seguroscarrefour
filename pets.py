import telegram
from Conf.settings import PET_ASSIST
from telegram import ReplyKeyboardMarkup


# 2° Iteração: O usuario envia o tipo de animal
def pets(update, context):
    #Coleta a mensagem do usuario
    Animal = update.message.text

    #Salva a infomação para uso externo
    context.user_data['animal'] = Animal


    reply_keyboard = [['1 ano','2 anos','3 anos','4 anos','5 anos','6 anos','7 anos']]
    update.message.reply_text(
            'Uall! Vamos ver a idade do seu <b>'+Animal+'</b>\n\n'
            '<i>*Por enquanto, garantimos assistência somente para pets com até 7 anos</i>',
                reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
                parse_mode=telegram.ParseMode.HTML)

#3° Iteração Condicional: Caso o usuário escolheu moto, salva as cilindradas e pergunta o ano do veículo
def OpcoesPets(update, context):
    # Salvando as cilindradas para uso externo
    idadeAnimal = update.message.text
    context.user_data['idadeAnimal'] = idadeAnimal

    #Retorna o veículo escolhido na função anterior
    Animal = context.user_data['animal']

   # Retorna o usuário loggado no telegram
    user = update.message.from_user


    update.message.reply_text('Muito bem Sr(a). <b>'+user.first_name+' </b>temos as seguintes opções para o seu  '
        '<b>'+Animal+'</b>, de <b>'+idadeAnimal+'</b>:',parse_mode=telegram.ParseMode.HTML)

    update.message.reply_text('<b>Opção 1:</b> AmigoO Pet Assist',parse_mode=telegram.ParseMode.HTML)
    update.message.reply_photo(PET_ASSIST)

    # Fim do trecho resultados de cotações

    #Pergunta ao usuário qual opção lhe agrada
    reply_keyboard = [['Opção 1: AmigoO']]
    update.message.reply_text(' Escolha a operadora para finalizar a aquisição do seguro:',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

def operadoraPet(update, context):
    # Coleta a mensagem do usuario
    Operadora = update.message.text

    # Salva a infomação para uso externo
    key = 'operadora'
    context.user_data[key] = Operadora
    #Mensagem Finaliza
    update.message.reply_text('Parabéns! Fez uma excelente escolha!!!\n\n '
                              'Escreva <b>\START</b> para fazer uma nova cotação. ',
                              parse_mode=telegram.ParseMode.HTML)


    # Exportanto JSON
    #Cotacao = []
    # Retorna os dados escolhidos nas iterações anteriores
    #user = update.message.from_user
    #Animal = context.user_data['animal']
    #Ano = context.user_data['idadeAnimal']
    #Nome = 'nome'
    #Cotacao.append({'User': user, 'Animal': Animal, 'Ano': Ano,
                   # 'Nome': Nome, 'Operadora': Operadora})

    #with open('cotacoes.json', 'w') as json_file:
       # json.dump(Cotacao, json_file, indent=3, ensure_ascii=False)