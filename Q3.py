# Função de registro dos números. Garante que o número seja inteiro.
def numero(b):
    while True:
        try:
            n = int(input(f'Digite o {b}º número: '))
        except Exception:
            print('Digite um número válido!')
        else: return n

# Função para calcular o mdc entre x (maior) e y (menor), usando o Algoritmo de Euclides em forma iterativa.
def mdc(y,x):
    while x != 0:
        r = y % x
        y = x
        x = r
    return y

# Aplica as regras descritas no enunciado.
m = [abs(numero(1)),abs(numero(2))]
if min(m) == 0:
    print(f'O mdc é de {max(m)}')
else:
    print(f'O mdc é de {mdc(min(m),max(m) % min(m))}')
