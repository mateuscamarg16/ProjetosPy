import numpy as np

print('Bem vindo a calculadora do Mateus')
print('A seguir, escolha a operação desejada')
x = input('Qual operação você deseja realizar? ')
y = int(input('Digite um valor: '))
z = int(input('Digite outro valor: '))

t = 1
k = np.nan

def calculadora(x, y, z):
  if x == 'adição':
    return print('O resultado da operação é:', (y+z))
  elif x == 'subtração':
    return print('O resultado da operação é:', (y-z))    
  elif x == 'multiplicação':
    return print('O resultado da operação é:', (y*z))
  elif x == 'divisão':
    return print('O resultado da operação é:', (y/z))

while t == 1:
    calculadora(x, y, z)
    k = input('Deseja realizar uma nova operação? ')
    if k == 'sim':
      x = input('Qual operação você deseja realizar? ')
      y = int(input('Digite um valor: '))
      z = int(input('Digite outro valor: '))
      t = 1
    else:
      t = 0
      print('Fim')
