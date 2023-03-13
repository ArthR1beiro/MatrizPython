# Defina o tamanho da matriz
n = 5

# Crie uma matriz triangular inferior com valores aleatórios
matriz_inf = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(i + 1):
        matriz_inf[i][j] = i + j + 1

# Crie uma matriz triangular superior com valores aleatórios
matriz_sup = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(i, n):
        matriz_sup[i][j] = i + j + 1

# Imprima as matrizes resultantes
print("Matriz triangular inferior:\n", matriz_inf)
print("Matriz triangular superior:\n", matriz_sup)

 # print('-='*30)
    # print(f"Matriz C {linhasA}x{colunasA}\n")
    # for l in range (linhasA):
    #     for c in range (colunasA):
    #         print(f'[{matrizA[l][c]+matrizB[l][c]}]', end='')
    #     print()