# Lista de atendimento, onde o usuário pode adicionar pessoas(com opção de adicionar quantas quiser), chamar a próxima pessoa da fila ou encerrar o sistema.
# Começo criando uma lista vazia onde atraves de um loop mantenho um sistema ativo com opções interativas
# Comandos obrigatorios utilizados: listas, input(), for, print(), pop(0)
# Comandos extras utilizados: while, if, elif, else, try, except e continue

lista = []

while True:
    try:
        print("Fila atual: ", lista)
        comando = str(input("\n SISTEMA DE ATENDIMENTO  \n 1 - Adicionar uma pessoa \n" \
        " 2 - Chamar o proximo \n 3 - Encerrar o sistema \n Qual opção deseja? "))
    except ValueError:
        print("=================================\n Nome inválido, tente novamente.\n=================================")
        continue
    if comando == ("1"):
        try:
            for i in range(int(input("Digite a quantidade de pessoas que voce quer adicionar: "))):
                print("Fila atual: ", lista)
                lista.append(input("Ola seja bem vindo, digite seu nome: "))
        except:
            print("=================================\n Comando invalido, tente novamente.\n================================= ")  
            continue    # Usei o try, except e continue para nao perder  os dados quando ocorrer um erro.
    elif comando == ("2"):
        try:
            pessoach = lista.pop(0)
            print(pessoach, " é a sua vez, por favor venha. ")
        except IndexError:      # Usei o try, except e continue caso a lista quando vazia nao gerar um erro.
            print("================================\n Lista de atendimento vazia.\n================================")
            continue
    elif comando == ("3"):
        break
    else:
        print("=================================\n Comando errado, tente novamente\n=================================")
