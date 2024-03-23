# Solicita para o usuário se ele deseja gravar as possibilidades num arquivo txt.
print('Número esperado: 16.483.600 = (30!/(27!*3!))²')
while True:
    n = input('Deseja gravar um arquivo ("registro.txt") com as possibilidades?(s/n) ')
    if not n.lower() in ('s','n'):
        print('Use "s" ou "n"!')
        continue
    if n.lower() == 's': n = True
    else: n = False
    break

a = []
b = []
# A partir de um grupo indo de 1 até 60, coloca os pares na lista a e os ímpares na lista b.
for k in range(1,61):
    if k % 2 == 0:
        a.append(k)
    else: b.append(k)

a2 = []
# A partir de a, une na lista a2 os números de índice k, j e h, nesta ordem. Sendo k>j>h, o que garante que não haja ordenações diferentes da mesma sequência.
for k in range(len(a)-2):
    for j in range(k+1,len(a)-1):
        for h in range(j+1,len(a)):
            a2.append([a[k],a[j],a[h]])

b2 = []
# Mesmo raciocínio para a lista b2.
for k in range(len(b)-2):
    for j in range(k+1,len(b)-1):
        for h in range(j+1,len(b)):
            b2.append([b[k],b[j],b[h]])

i = 0
# Como os elementos em a e b são diferentes, as composições a2 e b2 também o são. Portanto, basta combiná-las uma a uma para gerar todas as jogadas.
for k in a2:
    for j in b2:
        i += 1
        print(str(i)+' '+str(k[0]),j[0],k[1],j[1],k[2],j[2],sep=',')
        if n:
            with open('registro.txt', 'a') as arq:
                arq.write(str(i)+' '+str(k[0])+','+str(j[0])+','+str(k[1])+','+str(j[1])+','+str(k[2])+','+str(j[2])+'\n')
