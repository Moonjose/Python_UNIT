def ProcessMonthName(month):
    monthName = ''
    match month:
        case '01':
            monthName = 'Janeiro'
        case '02':
            monthName = 'Fevereiro'
        case '03':
            monthName = 'Março'
        case '04':
            monthName = 'Abril'
        case '05':
            monthName = 'Maio'
        case '06':
            monthName = 'Junho'
        case '07':
            monthName = 'Julho'
        case '08':
            monthName = 'Agosto'
        case '09':
            monthName = 'Setembro'
        case '10':
            monthName = 'Outubro'
        case '11':
            monthName = 'Novembro'
        case '12':
            monthName = 'Dezembro'
    return monthName

def SplitDate(dateToSplit):
    newDate =  dateToSplit.split('/')
    return newDate

date = input('Digite sua data de nascimento (dd/mm/yyyy): ')

print(f'Você nasceu em {SplitDate(date)[0]} de {ProcessMonthName(SplitDate(date)[1])} de {SplitDate(date)[2]}')