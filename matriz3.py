
linhasA = int(input("Digite o número de linhas da Matriz A: "))
while linhasA < 2:
    print("\n(O numero deve ser Igual ou maior que 2)")
    linhasA = int(input("Digite o número de linhas da Matriz A: "))

colunasA = int(input("\nDigite o número de colunas da Matriz A: "))
while colunasA < 2:
    print("\nO numero deve ser Igual ou maior que 2")
    colunasA = int(input("Digite o número de colunas da Matriz A: "))
    
linhasB = int(input("\nDigite o número de colunas da Matriz B: "))
while linhasB < 2:
    print("\n(O numero deve ser Igual ou maior que 2)")
    linhasB = int(input("Digite o número de linhas da Matriz B: "))

colunasB = int(input("\nDigite o número de colunas da Matriz B: "))
while colunasB < 2:
    print("\nO numero deve ser Igual ou maior que 2")
    colunasB = int(input("Digite o número de colunas da Matriz B: "))

matrizA = []

for i in range(linhasA):
    linhaA = []
    for j in range(colunasA):
        linhaA.append(0)
    matrizA.append(linhaA)

matrizB = []

for i in range(linhasB):
    linhaB = []
    for j in range(colunasB):
        linhaB.append(0)
    matrizB.append(linhaB)

if (colunasA == linhasB):
    print("É possivel realizar a multiplicação")
    print('-='*30)

    print("Digite os valores para Matriz A\n")
    for l in range (linhasA):
        for c in range (colunasA):
            matrizA[l][c] = int(input(f'Digite um valor para a{l+1}{c+1}: '))
            
    print("\nDigite os valores para Matriz B\n")
    for l in range (linhasB):
        for c in range (colunasB):
            matrizB[l][c] = int(input(f'Digite um valor para b{l+1}{c+1}: '))

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


    matrizC = [[0 for _ in range(len(matrizB[0]))] for _ in range(len(matrizA))]
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            for k in range(len(matrizB)):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]

    print('-='*30)
    print(f"C = A x B\nMatriz C {len(matrizC)}x{len(matrizC[0])}\n")

    for l in range (len(matrizC)):
        for c in range (len(matrizC[0])):
            print(f'[{matrizC[l][c]}]', end='')
        print()
    print("\nPrograma Finalizado.")

else:
    print('-='*30)
    print("\nNão é possivel realizar a multiplacação")
