# Cria a lista que contém as opções do menu.
a = ['Pizza Marguerita','Pizza de Calabresa','Pizza de Pepperoni','Pizza de Mussarela','Sair']

# Exibe o menu no formato requisitado.
print('Menu:')
for k in range(len(a)):
    print(f'{k+1} - {a[k]}')

while True:
    try:
        b = int(input('Digite sua escolha: '))
    except Exception: # Garante que a escolha seja um número inteiro.
        print('Digite um número válido!')
        continue
    if not int(b) in range(1,len(a)+1): # Garante que a escolha esteja dentro das alternativas (no caso, 1, 2, 3, 4 ou 5).
        print('Digite um número válido!')
        continue
    if b == len(a): # Termina a interação, caso o usuário escolha a última opção definida (no caso, 5).
        break
    print(f'Você escolheu: {a[int(b)-1]}.') # Exibe a escolha.
