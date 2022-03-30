print('Calculadora')
print(' + Adição')
print(' - Substração')
print(' * Multipliação')
print(' / Divisão')
print('Pressione outra tecla para sair')

op = input('Qual operação deseja fazer?')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite o primeiro valor:'))
    y = int(input('Digite o segundo valor:'))

if (op == '+'):
     res = x + y
     print('Resultado: {} + {} = {}'.format(x, y,res))
elif (op == '-'):
     res = x - y
     print('Resultado: {} - {} = {}'.format(x, y,res))
elif (op == '*'):
     res = x * y
     print('Resultado: {} * {} = {}'.format(x, y,res))
elif (op == '/'):
     res = x / y
     print('Resultado: {} / {} = {}'.format(x, y,res))
else:
    print('Operação inválida.')

print('Encerrando o programa...')