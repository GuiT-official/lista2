b = [[0,25],[26,50],[51,75],[76,100]]

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

con = []
# Pega todo intervalo j em b.
for j in b:
    i = 0
    # Realiza a verificação para todos os elementos k em a.
    for k in a:
        # Se k é maior ou igual ao limite inferior do intervalo e menor ou igual ao limite superior, conta +1.
        if j[1] >= k >= j[0]:
            i += 1
    # Depois, registra o número contado, em con.
    con.append(i)

for k in range(len(b)):
    print(f'{b[k]}: {con[k]}')
    