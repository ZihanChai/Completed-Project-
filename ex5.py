def function_names(parameters):
    ''' (io.TextIOWrapper) -> list of str
        Returns all the function' names inside of the input file.
        REQ: line <= lines
        >>>function_names('ex4.py')
           ['insert', 'up_to_first', 'cut_list']
    '''    
    my_file = open(parameters, 'r')  
    lines = my_file.readlines()
    names = []
    for line in lines:
        if line.startswith("def") == True:
            names.append(line[4:line.find('(')])                   
    my_file.close()    
    return names[:]

def justified(parameters):
    ''' (io.TextIOWrapper) -> boolean
        Returns a boolean which is True if and only if every line in that file is left-justified.
        REQ: line < len(lines)
        >>>justified('ex4.py')
           False
        '''     
    my_file = open(parameters, 'r')  
    lines = my_file.readlines()
    line = 0
    result = True
    while (line < len(lines)) and (result == True):
        if (lines[line].startswith(" ") == True):
            result = False
        else:
            line += 1    
    my_file.close()
    return result

    


