# Atividade p/ calcular porcentagem de desconto 2.1

preco = float (input('digite o preço do produto:'))
p = float (input('digite o percentual de desconto (0 -100)%: '))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é {}. Desconto de {}.'.format(preco,p))
print('Valor calculado de desconto: {}. Valor final do desconto: {}'.format(desconto, final))

print('    ')

# Atividade p/ calcular valor por KM rodado 2.2
km= int(input('Quantos Km foram percorridos?'))
dias = int(input('Por quantos dias ele foi alugado?'))

preco = 60 * dias + 0.15 * km
print('km = {}. Dias {}'. format(km, dias))
print('Valor a ser pago: {}'.format(preco))

print('    ')

# Atividade de String
frase = input('Digite uma frase:')
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2[-2:])