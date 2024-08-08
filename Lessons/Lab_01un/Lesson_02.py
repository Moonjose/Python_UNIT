import random

index = 0
dozensAmount = 0
dozens = []
surprise1 = []
surprise2 = []
lottoresult = []
correctNumbers = []
numToAccept = 15

#---------------- Methods
def testResults(listToIterate, resultName):
    correctNumbers = []
    for i in range(len(lottoresult)):  # 15 elements
        for j in range(len(listToIterate)):  # 18 elements
            if (lottoresult[i] == listToIterate[j]):
                correctNumbers.append(listToIterate[j])
    else:
        if len(correctNumbers) >= numToAccept:
            print('----------------------')
            print(f'A lista {resultName} acertou o mínimo de {numToAccept} numeros! - Todos os numeros corretos: {correctNumbers}')

def generateResults(startRange, endRange, listToAppend):
    for i in range(startRange, endRange):
        while True:
            randToAdd = random.randint(1, 25)
            if not (randToAdd in listToAppend):
                listToAppend.append(randToAdd)
                break

#---------------- Main 
while (True):
    print('--------------------------------------')
    dozensAmount = int((input('Digite a quantidade de dezenas que deseja marcar na primeira aposta: ')))
    if (not (15 <= dozensAmount <= 18)):
        print('--------------------------------------')
        print('Numero deve estar entre 15 e 18, digite novamente...')
    else:
        break

for i in range(dozensAmount):
    while (True):
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

#---------------- Generate the lotto results and fill the lists
generateResults(0, 18, surprise1)
generateResults(0, 18, surprise2)
generateResults(0, 15, lottoresult)

#---------------- Sort the lists
dozens.sort()
surprise1.sort()
surprise2.sort()
lottoresult.sort()

#---------------- Show the lists
print(f'Dezena escolhida: {dozens}')
print(f'Primeira surpresinha: {surprise1}')
print(f'Segunda surpresinha: {surprise2}')
print(f'Resultado da Loto Facil: {lottoresult}')

#---------------- Test the lists with lotto result
testResults(surprise1, 'Surpresinha 1')
testResults(surprise2, 'Surpresinha 2')
testResults(dozens, 'Dezenas escolhidas')
