UsersData = {}
counter = 1

def convertToMB(bytes):
    return bytes / 1048576

def CreateLog(data):
    for item in len(data):
        fileSystem = open('log.txt', 'w')
        fileSystem.write(f'{data[item]} - ')
        fileSystem.close()


while True:
    name = input('Digite o nome do usuário: ')
    byteAmount = float(input('Digite o numero de bytes usado: '))
    UsersData.append({name:byteAmount})
    choice = input('Deseja sair? [S/N]')
    if(choice == 'S'):
        break

CreateLog(UsersData)
