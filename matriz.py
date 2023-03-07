matriz = []
matriz_inf = []
matriz_sup = []
linhas = 0
colunas = 0

linhas = int(input("Digite o número de linhas e colunas da Matriz Quadrada: "))
colunas = linhas

while linhas < 3:
    print("\n(O numero deve ser Igual ou maior que 3)")
    linhas = int(input("Digite o número de linhas e colunas da Matriz Quadrada: "))
    colunas = linhas

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)
    matriz.append(linha)
    
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)
    matriz_sup.append(linha)
    
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)
    matriz_inf.append(linha)

 
for l in range (linhas):
    for c in range (colunas):
        matriz[l][c] = int(input(f'Digite um valor para a{l+1}{c+1}: '))
        matriz_inf[l][c] = matriz[l][c]
        matriz_sup[l][c] = matriz[l][c]

print('-='*30)
print(f"Matriz Quadrada {linhas}x{colunas}\n")
for l in range (linhas):
    for c in range (colunas):
        print(f'[{matriz[l][c]}]', end='')
    print()

print('-='*30)
print(f"Matriz Triangular Superior {linhas}x{colunas}\n")
for l in range (linhas):
    for c in range (colunas):
        if(l>c):
            matriz_sup[l][c] = 0
        print(f'[{matriz_sup[l][c]}]', end='')
    print()

print('-='*30)
print(f"Matriz Triangular Inferior {linhas}x{colunas}\n")
for l in range (linhas):
    for c in range (colunas):
        if(c>l):
            matriz_inf[l][c] = 0
        print(f'[{matriz_inf[l][c]}]', end='')
    print()

print("\nPrograma encerrado, obrigado por ultilizar.")