import math
# Função de registro do número. Também garante que o número declarado seja do tipo float.
def numero():
    while True:
        try:
            n = float(input(f'Digite o número: '))
        except Exception:
            print('Digite um número válido!')
        else: return n

# Função para achar o menor número primo que é maior ou igual ao argumento n.
def maior(n):
    # Devido à limitações da função range, a metodologia empregada só funciona para números maiores que 2.
    if n > 2:
        n = math.ceil(n) # Arredonda n pra cima.
        i = 0
        while True:
            # Apenas se é necessário verificar a primalidade de n+i com os potenciais múltiplos indo de 2 até a metade dele arredondada pra cima.
            for k in range(2,math.ceil((n+i)/2)+1):
                if (n+i) % k == 0:
                    i += 1 # Caso exista um múltiplo com n+i, aumenta i em 1 e termina a iteração do for, com o while repetindo o processo para n+i.
                    break
                elif k == math.ceil((n+i)/2): # Se k estiver na última iteração e o if anterior não tiver sido executado, retorna n+i (o número primo requisitado).
                    return n+i
    else:
        # No caso de n <= 2, a resposta sempre será 2.
        return 2

# Função para achar o maior número primo que é menor ou igual ao argumento n.
def menor(n):
    # Devido à limitações da função range, a metodologia empregada só funciona para números maiores que 3.
    if n >= 3:
        n = math.floor(n) # Arredonda n pra baixo.
        i = 0
        while True:
            # Apenas se é necessário verificar a primalidade de n+i com os potenciais múltiplos indo de 2 até a metade dele arredondada pra cima.
            for k in range(2,math.ceil((n+i)/2)+1):
                if (n+i) % k == 0:
                    i -= 1 # Caso exista um múltiplo com n+i, decresce i em 1 e termina a iteração do for, com o while repetindo o processo para n+i.
                    break
                elif k == math.ceil((n+i)/2): # Se k estiver na última iteração e o if anterior não tiver sido executado, retorna n+i (o número primo requisitado).
                    return n+i
    elif n >= 2:
        return 2
    else:
        # No caso de n <= 2, a resposta sempre será 2.
        return 'Não existe.'
            
n = numero()
print(f'Menor número primo que é maior ou igual a {n}: {maior(n)}')
print(f'Maior número primo que é menor ou igual a {n}: {menor(n)}')
