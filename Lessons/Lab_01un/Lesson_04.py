import random
lines = []
errors = 0
correctLetters = []
currentWord = ''

words = {
        'Processador': 'Cérebro de um computador',
        'Monitor': 'Dispositivo usado para mostrar imagem' ,
        'Mouse': 'Dispositivo usado para controlar o pontenteiro do computador',
        'Placa-Mãe': 'Peça que une os componentes de um computador',
        'Gabinete': 'Parte externa do computador que o guarda e o projete',
        'Kernel': 'Parte mais profunda do processador que comunica os softwares e o hardware',
        'Placa de video': 'Componente responsável por renderizar o gráfico no computador',
        'Caixa de som': 'Dispositivo que emite som',
        'Sistema Operacional': 'Software que gerencia os recursos de um computador e faz a comunicação entre usuário e os softwares'
        }

def GenerateLines(lines, randomKey):
    for i in range(len(randomKey)):
        lines.append(' ' if randomKey[i] == ' ' else '_')

    newLines = ''.join(lines) # Junta todo o conteúdo da lista e retorna apenas para o print inicial do programa
    return newLines

def ReplaceIndexes(letter): 
    for i in range(0, len(randomKey)):
        if randomKey[i] == letter:
            lines[i] = letter

    newLines = ''.join(lines) # Junta todo o conteúdo da lista e retorna para printar o estado da palavra atual
    return newLines
    
keys = list(words.keys())
randomKey = random.choice(keys) # Escolhe uma palavra aleatória da lista

# Para ver a palavra escolhida aleatoriamente (hack)
# print(randomKey)

startLines = GenerateLines(lines, randomKey) # Gera e printa as linhas iniciais baseado na palavra (ex: Palavra Kernel gera -> ------)
print(f'Dica: {words[randomKey]}')
print()
print(startLines)
print()

while True:
    
    choiceSelected = input('Insira uma letra: ')
    if not (choiceSelected in randomKey): # Se a letra informada não está na palavra da forca
       print(f'Letra errada! você ainda tem {2 - errors} chances...')
       print(currentWord if currentWord else startLines)
       errors = errors + 1
    elif (choiceSelected in correctLetters): # Se a letra informada já foi escolhida antes
        print('Você ja escolheu essa letra!...')
        print(currentWord if currentWord else startLines)
    else: # Se a letra informada está na palavra da forca (Case Sensitive)
        currentWord = ReplaceIndexes(choiceSelected) # Troca o caractere das linhas '-' pela letra correta na posição devida 
        print(currentWord if currentWord else startLines)
        correctLetters.append(choiceSelected)
        if not('_' in lines):
            print('Você venceu!!')
            break
    if errors == 3:
        print('Você errou 3x, fim de jogo!')
        break
