def compare_strings(string1, string2):
    if not isinstance(string1, str) and isinstance(string2, str):
        return 0
    else:
        if string1 == string2:
            return 1
        elif string2 == 'learn':
            return 3
        elif len(string1) > len(string2):
            return 2
        
cs = compare_strings('','')
print(cs)            