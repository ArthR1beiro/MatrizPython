matriz = []

for l in range (0, 4):
    for c in range (0, 4):
        matriz[l][c] = int(input(f'Digite um valor para a{l+1}{c+1}: '))
    

print('-='*30)
print("Matriz Quadrada\n")
for l in range (0, 4):
    for c in range (0, 4):
        print(f'[{matriz[l][c]}]', end='')
    print()
