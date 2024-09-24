nome = input("Digite o nome do usuário: ")
birthday = input("Digite a data de nascimento (DD/MM/AAAA): ")
cpf = input("DIgite o CPF: ")
creditCardLimit = input("Digite o limite do cartão de crédito: ")

nome = nome.rjust(30, "-")
print(nome.title())

birthday = birthday.rjust(30, "-")
print(birthday)

cpf = cpf.rjust(30, "-")
print(cpf)

creditCardLimit = creditCardLimit.rjust(30, "-")
print(creditCardLimit)