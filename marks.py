school = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '5b', 'scores': [5,4,4,5,2]}, {'school_class': '6c', 'scores': [5,5,5,5,5]}, {'school_class': '7a', 'scores': [2,2,2,2,2]},]    

def school_average(list):
    count = 0
    for i in list:
        for j in i['scores']:
            count += j
    school_average = count / len(list) / 5
    return school_average

def class_average(list):
    for i in list:
        count = 0
        for j in i['scores']:
            count += j
        print (i['school_class'], count / 5)

class_average(school)


print(school_average(school))   



