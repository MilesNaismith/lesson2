def compare_strings(string1, string2):
    if not isinstance(string1, str) or not isinstance(string2, str):
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string2 == 'learn':
        return 3    
        
cs = compare_strings('11231313','learn')
print(cs)            