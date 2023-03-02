linhasA = int(input("Digite o número de linhas da Matriz A: "))
colunasA = int(input("Digite o número de colunas da Matriz A: "))

matrizA = []

for i in range(linhasA):
    linhaA = []
    for j in range(colunasA):
        linhaA.append(0)
    matrizA.append(linhaA)


linhasB = int(input("Digite o número de linhas da Matriz B: "))
colunasB = int(input("Digite o número de colunas da Matriz B: "))

matrizB = []

for i in range(linhasB):
    linhaB = []
    for j in range(colunasB):
        linhaB.append(0)
    matrizB.append(linhaB)


if (linhasA == colunasB):
    print("É possivel realizar a soma")
else:
    print("Não é possivel realizar a soma")

# for l in range (0, 4):
#     for c in range (0, 4):
#         matriz[l][c] = int(input(f'Digite um valor para a{l+1}{c+1}: '))
    

print('-='*30)
print(f"Matriz A {linhasA}x{colunasA}\n")
for l in range (linhasA): 
    for c in range (colunasA):
        print(f'[{matrizA[l][c]}]', end='')
    print()

print('-='*30)
print(f"Matriz B {linhasB}x{colunasB}\n")
for l in range (linhasB):
    for c in range (colunasB):
        print(f'[{matrizB[l][c]}]', end='')
    print()


    