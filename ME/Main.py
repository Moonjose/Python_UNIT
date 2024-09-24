from Functions import *
import random
import time

# Begin Play
ClearTerminal()

# Stores the player names
player1['name'] = input("Digite o nome do primeiro jogador: ")
player2['name'] = input("Digite o nome do segundo jogador: ")

# Pick a random symbol to players
randomSymbol = random.choice(symbols)
player1['symbol'] = randomSymbol
symbols.remove(randomSymbol)

randomSymbol = random.choice(symbols)
player2['symbol'] = randomSymbol
symbols.remove(randomSymbol)

# Initial Print Game State
ClearTerminal()
print(f'O jogador {player1['name']} escolhe ({player1['symbol']}) e o jogador {player2['name']} escolhe ({player2['symbol']})')
print()
print('Iniciando jogo...')
time.sleep(2)
ClearTerminal()
PrintGame()

# GAME LOOP
while True:

    # Loop Player 1 
    currentPlayer = player1['symbol']
    while True:
        player1Choice = input(f'{player1['name']}, digite onde vai sua jogada.. (ex: 0,2): ')
        player1Choices = player1Choice.split(',')
        player1ChoiceX = int(player1Choices[0])
        player1ChoiceY = int(player1Choices[1])

        if(IsEmptyCoord(player1ChoiceX, player1ChoiceY)):
            matriz[player1ChoiceX][player1ChoiceY] = player1['symbol']
            PrintGame()
            break
        else: 
            ClearTerminal()
            PrintGame()
            print("Posição inválida, tente novamente!")

    ClearTerminal()
    PrintGame()       

    # CheckMatch
    if(HasWinner(matriz, currentPlayer)):
        print(f'{GetPlayerBySymbol(currentPlayer)} venceu!')
        PlayerScore(player1)
        print()
        GenerateLog()
        choice = input('Jogar novamente? [S/N]')
        if(choice == 'S'):
            ResetGame()
            ClearTerminal()
            PrintGame() 
            continue
        else:
            break
    elif(IsDraw()):
        print('Empate !')
        print()
        GenerateLog()
        choice = input('Jogar novamente? [S/N]')
        if(choice == 'S'):
            ResetGame()
            ClearTerminal()
            PrintGame() 
            continue
        else:
            break

    # Loop Player 2
    currentPlayer = player2['symbol']
    while True:
        player2Choice = input(f'{player2['name']}, digite onde vai sua jogada.. (ex: 0,2): ')
        player2Choices = player2Choice.split(',')
        player2ChoiceX = int(player2Choices[0])
        player2ChoiceY = int(player2Choices[1])

        if(IsEmptyCoord(player2ChoiceX, player2ChoiceY)):
            matriz[player2ChoiceX][player2ChoiceY] = player2['symbol']
            PrintGame()
            break
        else: 
            ClearTerminal()
            PrintGame()
            print("Posição inválida, tente novamente!")

    ClearTerminal()
    PrintGame()

    # CheckMatch
    if(HasWinner(matriz, currentPlayer)):
        print(f'{GetPlayerBySymbol(currentPlayer)} venceu!')
        PlayerScore(player2)
        print()
        GenerateLog()
        choice = input('Jogar novamente? [S/N]')
        if(choice == 'S'):
            ResetGame()
            ClearTerminal()
            PrintGame() 
            continue
        else:
            break
    elif(IsDraw()):
        print('Empate !')
        print()
        GenerateLog()
        choice = input('Jogar novamente? [S/N]')
        if(choice == 'S'):
            ResetGame()
            ClearTerminal()
            PrintGame() 
            continue
        else:
            break
