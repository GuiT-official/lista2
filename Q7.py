# Garante que n seja do tipo float.
while True:
    try:
        n = float(input('Digite um número positivo: '))
    except Exception:
        print('Digite um número positivo!')
        continue
    else:
        # Garante que n seja positivo.
        if n == 0 or n/abs(n) == -1:
            print('Digite um número positivo!')
            continue
        break

# Aplica o método de aproximações sucessivas de Newton até a vigésima aproximação, como requisitado.
i = 0
x = n/2
while i != 20:
    print(i+1,' ',x)
    x += -(x**2-n)/(2*x)
    i += 1