school = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '5b', 'scores': [5,4,4,5,2]}, {'school_class': '6c', 'scores': [5,5,5,5,5]}, {'school_class': '7a', 'scores': [2,2,2,2,2]},]    

def school_average(catalog):
    makrs_summ = 0
    count_pupil = 0
    for class_info in catalog:
        for mark in class_info['scores']:
            makrs_summ += mark
            count_pupil += 1
    school_average_mark = makrs_summ / count_pupil
    return school_average_mark

def class_average(catalog):
    for class_info in catalog:
        makrs_summ = 0
        count_pupil = 0
        for mark in class_info['scores']:
            makrs_summ += mark
            count_pupil += 1
        print (class_info['school_class'], makrs_summ / count_pupil)

class_average(school)


print(school_average(school))   
