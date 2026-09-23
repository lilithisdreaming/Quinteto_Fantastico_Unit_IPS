# Lista de atendimento, onde o usuário pode adicionar pessoas(com opção de adicionar quantas quiser), chamar a próxima pessoa da fila ou encerrar o sistema.
# Começo criando uma lista vazia onde atraves de um loop mantenho um sistema ativo com opções interativas
# Comandos obrigatorios utilizados: listas, input(), for, print(), pop(0)
# Comandos extras utilizados: while, if, elif, else
lista = []

while True:
    print("Fila atual: ", lista)
    comando = input("\n SISTEMA DE ATENDIMENTO  \n 1 - Adicionar uma pessoa \n" \
    " 2 - Chamar o proximo \n 3 - Encerrar o sistema \n Qual opção deseja? ")
    if comando == ("1"):
        for i in range(int(input("Digite a quantidade de pessoas que voce quer adicionar: "))):
         print("Fila atual: ", lista)
         lista.append(input("Ola seja bem vindo, digite seu nome: "))
    elif comando == ("2"):
         pessoach = lista.pop(0)
         print(pessoach, " é a sua vez, por favor venha. ")
    elif comando == ("3"):
        break
    else:
        print("Comando errado, tente novamente")
