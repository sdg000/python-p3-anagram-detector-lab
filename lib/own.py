def check(a, b= []):

    sorted_word = ''.join(sorted(a))

    new = []


    for i in b:
        if(sorted_word == ''.join(sorted(i))):
            new.append(i)
        
    print(new)
    print('come')


check('you', ['come', 'owu', 'you', 'tot', 'yuu'])