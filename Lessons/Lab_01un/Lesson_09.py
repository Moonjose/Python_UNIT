from ..libs import Utilities_09 as util

temp1 = input("Digite a primeira temperatura: ")
temp2 = input("Digite a segunda temperatura: ")

temp1Type = util.findTempType(temp1)
temp2Type = util.findTempType(temp2)

if (temp1Type == temp2Type):
    print(f'A maior temperatura é: {temp1 if temp1 > temp2 else temp2 }')
#elif (temp1Type == 'C'): 
