matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matrizinf = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
matrizsup = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for l in range (0, 4):
    for c in range (0, 4):
        matriz[l][c] = int(input(f'Digite um valor para a{l+1}{c+1}: '))
        matrizsup[l][c] = matriz[l][c]
        matrizinf[l][c] = matriz[l][c]



print('-='*30)
print("Matriz Quadrada\n")
for l in range (0, 4):
    for c in range (0, 4):
        print(f'[{matriz[l][c]}]', end='')
    print()

print('-='*30)
for l in range (0, 4):
    for c in range (0, 4):
        if(l>c):
            matrizinf[l][c] = 0

print("Matriz Triangular Superior\n")
for l in range (0, 4):
    for c in range (0, 4):
        print(f'[{matrizsup[l][c]}]', end='')
    print()

print('-='*30)
for l in range (0, 4):
    for c in range (0, 4):
        if(c>l):
            matrizinf[l][c] = 0

print("Matriz Triangular Inferior\n")
for l in range (0, 4):
    for c in range (0, 4):
        print(f'[{matrizinf[l][c]}]', end='')
    print()

print("\nPrograma encerrado, obrigado por ultilizar.")