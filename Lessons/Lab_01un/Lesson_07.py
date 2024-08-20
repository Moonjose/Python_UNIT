def convertHour(hours):
    hoursSplited = hours.split(':')
    hour = int(hoursSplited[0])
    if(hour < 12 ):
        return f'Hora convertida: {hours} AM'
    elif(hour>12):
        return f'{hour - 12}:{hoursSplited[1]}'
    else: 
        return hours
    
userHour = input('Digite a hora no formato 24h: ')
print(convertHour(userHour))

