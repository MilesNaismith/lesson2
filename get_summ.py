def get_summ(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)
    except ValueError:
        return 'Требуется указать числа'    
    return num_one + num_two

print(get_summ('qwe','-564'))    