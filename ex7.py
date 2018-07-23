def create_dict(input_file):
    ''' (io.TextIOWrapper) -> dict of {str: [str, str, str, int, str]}
        Returns a dictionary that maps a string to a list of strings and ints,
        by taking the parameter as an open file handle and converte the text to 
        dictionary: the username as the key and and the value being a list of 
        [last name, first name, e-mail, age, gender].
        >>>create_dict(open('ex7 data.txt', 'r'))
        {'asmith': ('Smith', 'Alice', 'alice.smith@utsc.utoronto.ca', '31', 'F'), 'bharrington': ('Harrington', 'Brian', 'brian.harrington@utsc.utoronto.ca', '33', 'M'), 'ddrumpf': ('Drumpf', 'Donald', 'tinyhands@buildawall.net', '70', 'F'), 'cmangler': ('Mangler', 'Code', 'cm@mangler.net', '103', 'F'), 'hclinton': ('Clinton', 'Hillary', 'publicaddress@privateserver.notgov', '69', 'F'), 'ajones': ('Jones', 'Alice', 'alice@alicejones.net', '44', 'F')}
    '''    
    #read the file line by line
    lines = input_file.readlines()
    #create an empty dictionary    
    data_set = {}
    #copy the file to the list line by line
    for line in lines:
        c = line.strip('\n').split(' ')
        data_set[c[0]] = c[2], c[1], c[5], c[3], c[4]
    return data_set

def update_field(dictionary, username, field_name, new_value):
    '''( dict of {str: [str, str, str, int, str]}, str, str, str or int) -> None
       Return None type but change the dictionary by match the key's value name 
       and converse the old value by the new value
       >>> my_dict = {'sclause':['Clause', 'Santa', 'santa@christmas.np', 450, 'M']}
       >>> update_field(my_dict, 'sclause', 'AGE', 999)
       >>> my_dict == {'sclause': ['Clause', 'Santa', 'santa@christmas.np', 999, 'M']}
    '''
    # match the value name in the dictionary and the parameter, then change the value of speacfic key
    if(field_name == 'LAST'):
        dictionary[username][0] = new_value
    elif(field_name == 'FIRST'):
        dictionary[username][1] = new_value
    elif(field_name == 'E-MAIL'):
        dictionary[username][2] = new_value
    elif(field_name == 'AGE'):
        dictionary[username][3] = new_value
    elif(field_name == 'GENDER'):
        dictionary[username][4] = new_value