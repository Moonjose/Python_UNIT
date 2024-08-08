import random

index = 0
dozensAmount = 0
dozens = []
surprise1 = []
surprise2 = []
lottoresult = []
correctNumbers = []
numToAccept = 10

while(True):    
    print('--------------------------------------')
    dozensAmount = int((input('Digite a quantidade de dezenas que deseja marcar na primeira aposta: ')))
    if (not(15 <= dozensAmount <= 18)):
        print('--------------------------------------')
        print('Numero deve estar entre 15 e 18, digite novamente...')
    else:
        break

for i in range(dozensAmount):
    while(True):
        print('--------------------------------------')
        numToAdd = int(input(f'Digite o {index + 1}° número: '))

        if not (1 <= numToAdd <= 25):
            print('--------------------------------------')
            print('Dezena deve estar entre 1 e 25, digite novamente...')
        elif numToAdd in dozens:
           print('--------------------------------------')
           print('Essa dezena já foi escolhida, escolha outra...')
        else:
             dozens.append(numToAdd)
             index += 1
             break


for i in range(0, 18):
    while True:
        randToAdd = random.randint(1, 25)
        if not (randToAdd in surprise1):
            surprise1.append(randToAdd)
            break

for i in range(0, 18):
    while True:
        randToAdd = random.randint(1, 25)
        if not (randToAdd in surprise2):
            surprise2.append(randToAdd)
            break

for i in range(0, 15):
    while True:
        randToAdd = random.randint(1, 25)
        if not (randToAdd in lottoresult):
            lottoresult.append(randToAdd)
            break
    
dozens.sort()
surprise1.sort()
surprise2.sort()
lottoresult.sort()

print(f'Primeira dezena escolhida: {dozens}')
print(f'Primeira surpresinha: {surprise1}')
print(f'Segunda surpresinha: {surprise2}')
print(f'Resultado da Loto Facil: {lottoresult}')

correctNumbers = []
for i in range(len(lottoresult)): #15 elements
    for j in range(len(surprise1)): # 18 elements
        if(lottoresult[i] == surprise1[j]):
            correctNumbers.append(surprise1[j])
else:
    if len(correctNumbers) >= numToAccept:
        print('----------------------')
        print(f'A surpresinha 1 acertou o mínimo de {numToAccept} numeros! - Todos os numeros corretos: {correctNumbers}')

correctNumbers = []
for i in range(len(lottoresult)): #15 elements
    for j in range(len(surprise2)): # 18 elements
        if(lottoresult[i] == surprise2[j]):
            correctNumbers.append(surprise2[j])
else:
    if len(correctNumbers) >= numToAccept:
        print('----------------------')
        print(f'A surpresinha 2 acertou o mínimo de {numToAccept} numeros! - Todos os numeros corretos: {correctNumbers}')

correctNumbers = []
for i in range(len(lottoresult)): #15 elements
    for j in range(len(dozens)): # 18 elements
        if(lottoresult[i] == dozens[j]):
            correctNumbers.append(dozens[j])
else:
    if len(correctNumbers) >= numToAccept:
        print('----------------------')
        print(f'A dezena escolhida acertou o mínimo de {numToAccept} numeros! - Todos os numeros corretos: {correctNumbers}')

