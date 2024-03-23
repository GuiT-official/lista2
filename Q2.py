# Garante que a quantia de números n declarada seja do tipo inteiro.
while True:
    try:
        n = int(input('Digite a quantia de números que pretende digitar: '))
    except Exception:
        print('Digite um número válido!')
    else: break

# Função de registro dos números. Também garante que o número declarado seja do tipo float.
def numero():
    while True:
        try:
            n = float(input(f'Digite o {len(a)+1}º número: '))
        except Exception:
            print('Digite um número válido!')
        else: return n

# Requisita os números até ter n números.
a = []
while len(a) != n:
    a.append(numero())

# Soma todas as frequências de cada elemento na lista a.
i = 0
for k in a:
    i += a.count(k)

# Caso não haja repetição de elementos e a lista já esteja organizada do menor pro maior, entende a função como crescente. Caso contrário, entende como não crescente.
if i == len(a) and a == sorted(a):
    print('A sequência declarada é crescente!')
else:
    print('A sequência declarada não é crescente!')
