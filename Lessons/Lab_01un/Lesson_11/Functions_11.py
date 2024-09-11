def CreateFile(fileName):
    file = open(f'{fileName}.txt', 'w')

def Tabuada(fileN):
    with open(fileN, "w") as arq_tab:
        arq_tab.write('Teste')

def convertToMB(bytes):
    return bytes / 1048576

def CreateLog(data):
    for item in data:
        fileSystem = open('log.txt', 'w')
        fileSystem.write(f'{item.key} - {convertToMB(item.value)}')
        fileSystem.close()
