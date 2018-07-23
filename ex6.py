def copy_me(input_list):
    ''' (list) -> list
        Returns a copy of the input_list that convert all the string letters to upper-case; increase the integer and floats increase the value by one; booleans are negated; lists be replaced by string 'List'
        >>>copy_me([1,2,3,'string',True])
           [2,3,4,'STRING',False]
    '''      
    l_copy = []
    for e in input_list:
        if type(e) == str:
            l_copy.append(e.upper())
        elif(type(e) == int or type(e) == float):
            l_copy.append(e + 1)
        elif(type(e) == bool):
            if(e == True):
                l_copy.append(False)
            elif(e == False):
                l_copy.append(True)
        elif(type(e) == list):
            l_copy.append('List')
    return l_copy

def mutate_me(input_list):
    ''' (list) -> None
        Returns None and change the input_list by convert all the string letters to upper-case; increase the integer and floats' value by one; booleans are negated; lists be replaced by string 'List'
        >>>mutate_me([1,2,3,'string',True])
           None
    '''      
    l = input_list 
    for e in range(len(input_list)):
        if(type(input_list[e]) == str):
            l[e] = input_list[e].upper()
        elif(type(input_list[e]) == int or type(input_list[e]) == float):
            l[e] = input_list[e] + 1
        elif(type(input_list[e]) == bool):
            if(input_list[e] == True):
                l[e] = False
            elif(input_list[e] == False):
                l[e] = True
        elif(type(input_list[e]) == list):
            l[e] = 'List'
    return None