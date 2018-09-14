age = input('Введите свой возраст, пожалуйста: ')

def what_is_your_duty(age):
    try:
        age = int(age)
    except ValueError:
        return 'Требуется ввести число'
    if age < 0:
        return 'Вот сначала родись, а потом уже программировать будешь!'      
    elif age < 7:
        return 'Тебе следует учиться в детском саду'
    elif age < 17:
        return 'Тебе следует учиться в школе'
    elif age < 23:
        return 'Тебе следует учиться в ВУЗе'
    else:
        return 'Тебе следует работать' 

wd = what_is_your_duty(age)
print(wd)       