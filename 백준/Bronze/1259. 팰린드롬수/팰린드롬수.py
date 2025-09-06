while True:
    inp = input()
    
    if inp == '0':
        break
    
    if inp == inp[::-1]:
        print('yes')
    else:
        print('no')