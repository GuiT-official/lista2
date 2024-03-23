# Garante que n seja do tipo inteiro.
while True:
    try:
        n = int(input('Digite um número inteiro positivo: '))
    except Exception:
        print('Digite um número inteiro positivo!')
        continue
    else:
        # Garante que n seja positivo.
        if n == 0 or n/abs(n) == -1:
            print('Digite um número inteiro positivo!')
            continue
        break

for k in range(1,n+1):
    print(' '*(k-1)+str(k))
