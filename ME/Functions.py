import os

# Data
matriz = [[' ' for x in range(3)] for x in range(3)]
player1 = {'name' : '', 'pts': 0, 'symbol' : ''}
player2 = {'name' : '', 'pts': 0, 'symbol' : ''}
symbols = ['X', 'O']
currentPlayer = ''

# Print the actual game state
def PrintGame():
    print(f'{player1['name']}[{player1['symbol']}] ({player1['pts']} pts) vs {player2['name']}[{player2['symbol']}] ({player2['pts']} pts)')
    print()
    print('    0 ,  1 ,  2 ')
    for x in range(len(matriz)):
        print(f'{x} {matriz[x]}')
    print()

# Returns the winner given a symbol
def GetPlayerBySymbol(symbol):
    if player1.get('symbol') == symbol:
        return player1.get('name')
    elif player2.get('symbol') == symbol:
        return player2.get('name')
    return None

# Clear the terminal
def ClearTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Check if the board coordinate is a valid coord
def IsEmptyCoord(coord1, coord2):
    if not (0 <= coord1 <= 2 and 0 <= coord2 <= 2):
        return False
    if not matriz[coord1][coord2] == ' ':
       return False
    else:
        return True

# Check if has a winner
def HasWinner(board, player):
    winConditions = [
    [board[0][0], board[0][1], board[0][2]],
    [board[1][0], board[1][1], board[1][2]],
    [board[2][0], board[2][1], board[2][2]],
    # Colunas
    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    # Diagonais
    [board[0][0], board[1][1], board[2][2]],
    [board[0][2], board[1][1], board[2][0]]
    ]

    return [player, player, player] in winConditions
        
# Check if it is draw
def IsDraw():
    drawCounter = 0
    for line in matriz:
        for element in line:
            if(element != ' '):
                drawCounter = drawCounter + 1
    if drawCounter == 9:
        return True
    else:
        return False

# Reset the board
def ResetGame():
    global matriz 
    matriz[:] = [[' ' for x in range(3)] for x in range(3)]

# Score +1 to Winner
def PlayerScore(player):
    player['pts'] += 1

# Generate log to /logs as append 
def GenerateLog():
    with open('Logs/Games.txt', 'a') as log:
        log.write(f'{player1['name']}[{player1['symbol']}] ({player1['pts']} pts) vs {player2['name']}[{player2['symbol']}] ({player2['pts']} pts)\n')
        log.write('-------------------\n')
        log.writelines([f'{matriz[0][0]} | ' , f'{matriz[0][1]} | ', f'{matriz[0][2]}\n'])
        log.writelines([f'{matriz[1][0]} | ' , f'{matriz[1][1]} | ', f'{matriz[1][2]}\n'])
        log.writelines([f'{matriz[2][0]} | ' , f'{matriz[2][1]} | ', f'{matriz[2][2]}\n'])
        log.write('\n')