names = []
sex = []
sign = []
kilometers = []
days = []

while(True):
    
    names.append(input('Digite seu nome: '))
    sex.append(input('Digite seu sexo: '))
    sign.append(input('Digite a placa do carro: '))
    kilometers.append(float(input('Digite a quantidade de quilômetros que deseja: ')))
    
    days.append(int(input('Digite a quantidade de dias que irá contratar: ')))

    choice = input('Sair? [S/N]')
    if (choice == 'S'):
        break
    
for i in range(len(names)):
     print(f'Placa do carro: {sign[i]}, Valor total: {(70 * days[i] + 0.10 * kilometers[i])}')
  