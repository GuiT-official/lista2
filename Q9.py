# Garante que c seja do tipo inteiro.
while True:
    try:
        c = int(input('Digite um número inteiro positivo: '))
    except Exception:
        print('Digite um número inteiro positivo!')
        continue
    else:
        # Garante que n seja positivo.
        if c == 0 or c/abs(c) == -1:
            print('Digite um número inteiro positivo!')
            continue
        break

# Faz a iteração para todas as possibilidades para x1. Em seguida, itera todas as possibilidades de x2. Por fim, x3 só terá uma possibilidade.
i = 0
for k in range(c+1):
    for j in range(c-k+1):
        i += 1
        print(i,' ',k,'+',j,'+',c-k-j,'=',c)
