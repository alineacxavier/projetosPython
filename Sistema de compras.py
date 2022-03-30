# Atividade de escolhas
print('Escolha o que deseja comprar:')
print('1 - Maça')
print('2 - Banana')
print('3 - Morango')
produto = int(input('Qual a sua escolha?'))
qtd = int(input('Quantas unidades?'))
if (produto == 1):
     pagar = qtd * 3.6
     print('Você comprou {} maças. Total à pagar: {}'.format(qtd, pagar))

print('   ')

# Atividade
nome = input('Qual seu nome?')
idade = input('Qual sua idade?')
if (nome == 'Aline'):
    print('Olá, Aline!!')
elif idade < 18:
    print('Você não é a Aline! E é menor de idade! ;-;')
elif idade > 100:
    print('Diferente de você,  a Aline não é imortal! rs')
