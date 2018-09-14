def ask_user():
    vocabulary = {'Привет':'Привет!!', 
                  'Как дела?':'Хорошо', 
                  'Где бы ты хотел работать?': 'В Aperture Science', 
                  'Что делаешь?':'Программирую', 
                  'Кем бы ты хотел стать?':'ОБЧР(Огромным Боевым Человекоподобным Роботом)',
                 }
    try:              
        while True:
            frase = input('Человек: ')
            if frase in vocabulary:
                print('Программа: ' + vocabulary[frase])
            else:
                print('Программа: Я тебя не понимаю, попробуй сформулировать свой вопрос иначе')   
    except(KeyboardInterrupt):
        print('Пока!')
ask_user()
