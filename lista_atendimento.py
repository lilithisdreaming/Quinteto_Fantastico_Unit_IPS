# Sistema de atendimento interativo.
# Permite adicionar pessoas à fila, chamar o próximo da lista ou encerrar o programa.
# Usa uma lista para armazenar nomes e um loop while para manter o sistema ativo.
# Inclui tratamento de erros com try/except para evitar falhas em entradas inválidas.

lista = []

# Loop principal, mantem o sistema ativo.
while True:
    try:
        print("Fila atual: ", lista)
        comando = str(input("\n SISTEMA DE ATENDIMENTO  \n 1 - Adicionar uma pessoa \n" \
        " 2 - Chamar o proximo \n 3 - Encerrar o sistema \n Qual opção deseja? "))
    except ValueError:
        print("=================================\n Nome inválido, tente novamente.\n=================================")
        continue
    if comando == ("1"):   # Condição para adicionar pessoas à fila, com opção de repetir essa etapa N vezes.
        try:
            for i in range(int(input("Digite a quantidade de pessoas que voce quer adicionar: "))):
                print("Fila atual: ", lista)
                lista.append(input("Ola seja bem vindo, digite seu nome: "))
        except:
            print("=================================\n Comando invalido, tente novamente.\n================================= ")  
            continue    # Usei o try, except e continue para nao perder  os dados quando ocorrer um erro.
    elif comando == ("2"):  # Condição para chamar o primeiro da fila, retirando o seu nome.
        try:
            pessoach = lista.pop(0)
            print(pessoach, " é a sua vez, por favor venha. ")
        except IndexError:      # Usei o try, except e continue caso a lista quando vazia nao gerar um erro.
            print("================================\n Lista de atendimento vazia.\n================================")
            continue
    elif comando == ("3"):  # Condição para desligar o loop
        break
    else:
        print("=================================\n Comando errado, tente novamente\n=================================")
