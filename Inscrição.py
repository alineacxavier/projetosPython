from random import seed
from random import randint
print('***********MENU***********')
print('')
print('1 - Nova Inscrição')
print('2 - Visualizar Inscrição')
print('0 - Encerrar')
saida = int(input('Escolha uma opção: '))
if (saida != 1) and (saida != 2) and (saida != 0):
    print('Escolha uma opção válida!')
while (saida != '0'):
    if (saida == 1):
        seed(100)
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        tel = int(input('Digite seu telefone: '))
        curso = input('Digite seu curso: ')
        print('***********MENU***********')
        print('')
        print('1 - Nova Inscrição')
        print('2 - Visualizar Inscrição')
        print('0 - Encerrar')
        saida1 = input('Escolha uma opção: ')
        if (saida != 1) or (saida != 2) or (saida != 0):
            print('Escolha uma opção válida!')
        while (saida != '0'):
            if (saida1 == 2):
                lista = [randint(100,400),nome,email,tel,curso]