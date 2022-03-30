print('Hotel dos Animais')
print('')
print('Vamos começar!')
print('')
print('R - Rato / C - Cachorro / O - Osso / Q - Queijo / G - Gato')
print('Especificando as posições:')
print('')
print('[1,2,3,4]')
print('[5,6,7,8]')
print('Na Fase 1, o Jogador deve alocar o RATO e o GATO na seguinte matriz que represente os quartos:')
print('[*] [*] [ ] [G]')
print('[R] [ ] [*] [*]')
rato = input('em qual posição deseja alocar o Rato? ')
gato = input('em qual posição deseja alocar o Gato? ')
if rato != '3':
    print('Game Over!')
elif rato == '3':
    print('Você Acertou!')
elif gato != '6':
    print('Game Over')
elif gato == '6':
    print('Você acertou!')
elif (rato == '3') and (gato == '6'):
    print('Na Fase 2, o Jogador deve alocar o CÃO, CÃO E O OSSO na seguinte matriz que representa os quartos:')
    print('[ ] [*] [*] [*]')
    print('[*] [C] [ ] [ ]')
    cao = input('em qual posição deseja alocar o CÃO? ')
    cao2 = input('em qual posição deseja alocar o segundo CÃO? ')
    osso = input('em qual posição deseja alocar o OSSO? ')
    if cao != '1':
        print('Game Over!')
    elif cao == '1':
        print('Você Acertou!')
    if cao2 != '7':
        print('Game Over!')
    elif cao2 == '7':
        print('Você Acertou!')
    elif osso != '8':
        print('Game Over')
    elif osso == '8':
        print('Você acertou!')
    elif (cao == '1') and (cao2 == '7') and (osso == '8'):
        print('Na Fase 3, o Jogador deve alocar o GATO, RATO E O OSSO na seguinte matriz que representa os quartos:')
        print('[ ] [*] [*] [*]')
        print('[ ] [G] [ ] [*]')
        gato1 = input('em qual posição deseja alocar o GATO? ')
        rato1 = input('em qual posição deseja alocar o RATO? ')
        osso1 = input('em qual posição deseja alocar o OSSO? ')
        if gato1 != '1':
            print('Game Over!')
        elif gato1 == '1':
            print('Você Acertou!')
        if rato1 != '5':
            print('Game Over!')
        elif rato1 == '5':
            print('Você Acertou!')
        elif osso1 != '7':
            print('Game Over')
        elif osso1 == '7':
            print('Você acertou!')
        elif (gato1 == '1') and (rato1 == '5') and (osso1 == '7'):
            print(
                'Na Fase 4, o Jogador deve alocar o QUEIJO, QUEIJO E O OSSO na seguinte matriz que representa os quartos:')
            print('[ ] [ ] [ ] [*]')
            print('[*] [R] [*] [*]')
            queijo = input('em qual posição deseja alocar o QUEIJO? ')
            queijo2 = input('em qual posição deseja alocar o segundo QUEIJO? ')
            osso1 = input('em qual posição deseja alocar o OSSO? ')
            if gato1 != '1':
                print('Game Over!')
            elif gato1 == '1':
                print('Você Acertou!')
            if rato1 != '2':
                print('Game Over!')
            elif rato1 == '2':
                print('Você Acertou!')
            elif osso1 != '3':
                print('Game Over')
            elif osso1 == '3':
                print('Você acertou!')
