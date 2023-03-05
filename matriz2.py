
linhasA = int(input("Digite o número de linhas da Matriz A: "))
while linhasA < 2:
    print("\n(O numero deve ser Igual ou maior que 2)")
    linhasA = int(input("Digite o número de linhas da Matriz A: "))

colunasA = int(input("\nDigite o número de colunas da Matriz A: "))
while colunasA < 2:
    print("\nO numero deve ser Igual ou maior que 2")
    colunasA = int(input("Digite o número de colunas da Matriz A: "))
    
matrizA = []

for i in range(linhasA):
    linhaA = []
    for j in range(colunasA):
        linhaA.append(0)
    matrizA.append(linhaA)



print('-='*30)
print("Digite os valores para Matriz A\n")
for l in range (linhasA):
    for c in range (colunasA):
          matrizA[l][c] = int(input(f'Digite um valor para a{l+1}{c+1}: '))


print('-='*30)            
print(f"Matriz A {linhasA}x{colunasA}\n")
for l in range (linhasA): 
    for c in range (colunasA):
         print(f'[{matrizA[l][c]}]', end='')
    print()

print('-='*30)
print(f"Matriz A oposta {linhasA}x{colunasA}\n")
for l in range (linhasA): 
    for c in range (colunasA):
         print(f'[{-matrizA[l][c]}]', end='')
    print()

print('-='*30)
print(f"Matriz A transposta {linhasA}x{colunasA}\n")
for l in range (linhasA): 
    for c in range (colunasA):
         print(f'[{matrizA[c][l]}]', end='')
    print()

    

