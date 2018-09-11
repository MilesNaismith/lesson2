def ask_user():
    vocabulary = {'Привет':'Привет!!', 'Как дела?':'Хорошо', 'Где бы ты хотел работать?': 'В Aperture Science', 'Что делаешь?':'Программирую', 'Кем бы ты хотел стать?':'ОБЧР(Огромным Боевым Человекоподобным Роботом)'}
    while True:
        try:
            frase = input('Человек: ')
        except(KeyboardInterrupt):
            print('Пока!')
            break    
        if frase in vocabulary:
            print('Программа: ' + vocabulary[frase])
        else:
            print('Программа: Я тебя не понимаю, попробуй сформулировать свой вопрос иначе')   
ask_user()
