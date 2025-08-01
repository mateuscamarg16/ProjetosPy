print('Informe suas notas para saber se passou de ano!')

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))

nota_final = float(nota1 + nota2 + nota3 + nota4 / 4)

if nota_final < 20:
    print(f'Sua média final foi {nota_final}. Infelizmente você não passou.')
else:
    print(f'Sua média final foi {nota_final}. Parabéns, você passou.')
