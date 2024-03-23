import math
# Garante que n seja do tipo inteiro.
while True:
    try:
        n = int(input('Digite um número inteiro positivo para converter em binário: '))
    except Exception:
        print('Digite um número inteiro positivo!')
        continue
    else:
        # Garante que n seja positivo.
        if n == 0 or n/abs(n) == -1:
            print('Digite um número inteiro positivo!')
            continue
        break

# Função de conversão para binário.
def calcular(n):
    # Pega o maior expoente ao qual, quando elevado ao quadrado, ele chegue o mais próximo de n.
    i = math.floor(math.log2(n))
    k2 = 0
    x = ''
    k0 = i
    while True:
        # Vai adicionando 1s e 0s conforme necessário, na variável x.
        for k in range(i+2):
            if n-k2 == 0:
                x += '0'*k0 # Repete 0s à direita da variável x, k0 vezes.
                return x
            # Vai até o k exponente que, quando elevado ao quadrado, seja igual à n-k2.
            elif (n-k2) == 2**k:
                k2 += 2**k
                x += f'{"1":0>{k0-k}}' # Repete 0s à esquerda do 1, até que a string resultante seja de tamanho k0-k (a quantidade de zeros à adicionar sempre será de k0-k-1).
                k0 = k
                break
            # Vai até o k exponente + 1 que, quando elevado ao quadrado, chegue o mais próximo de n-k2.
            elif (n-k2) < 2**k:
                k2 += 2**(k-1)
                x += f'{"1":0>{k0-k+1}}' # Repete 0s à esquerda do 1, até que a string resultante seja de tamanho k0-k+1 (a quantidade de zeros à adicionar sempre será de k0-(k-1)-1).
                k0 = k-1
                break

print(f'Em base binária: {calcular(n)}')
