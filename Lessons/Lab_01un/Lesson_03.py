questions = []
answers = []
userAnswers = []
dictList = []

print('Cadastro de questões -----------------------')
questionsAmount = int(input('Digite a quantidade de questões que deseja cadastrar: '))

for i in range(0, questionsAmount):
    questions.append(input('Digite o enunciado da questão: '))
    choice = input('Digite a resposta para essa questão [V] ou [F]: ')
    answers.append(True if choice == 'V' else False)

while True:
    dict_answers = {
    'Name': '',
    'Answers': []
}
    print('Cadastro de usuário -----------------------')
    userAnswers = []
    name = input('Digite seu nome: ')
    dict_answers['Name'] = name
    print('Teste de conhecimentos -----------------------')

    for i in range(0, len(questions)):
        print('---------------------')
        print(questions[i])
        userChoice = input('Digite [V] para verdadeiro ou [F] para falso: ')
        userAnswers.append(True if userChoice == 'V' else False)

    dict_answers['Answers'] = userAnswers
    dictList.append(dict_answers)

    action = input('Sair? [S/N]')
    if (action == 'S'):
        break
        
print(dictList)

print('-------------------------------- RESULTADO --------------------------------')
print('Perguntas: ')
print()
for l in questions:
    print(l)

print()
print('Relatório --------------------------------')
for j in dictList:
    for h in range(len(j['Answers'])):
        print(f'{j['Name']} marcou {'Verdadeiro' if j['Answers'][h] == True else 'Falso'} na questão {h + 1} portanto {'ACERTOU' if j['Answers'][h] == answers[h] else 'ERROU'}')
    