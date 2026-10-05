# Sistema de atendimento interativo.
# Permite adicionar pessoas à fila, chamar o próximo da lista ou encerrar o programa.
# Usa uma lista para armazenar nomes e um loop while para manter o sistema ativo.
# Inclui tratamento de erros com try/except para evitar falhas em entradas inválidas.

lista = []

# Loop principal que mantém o sistema funcionando.
while True:
    try:
        print(f"Fila atual: {lista}")
        comando = input(
            "\nSISTEMA DE ATENDIMENTO\n"
            "1 - Adicionar pessoa\n"
            "2 - Chamar próximo\n"
            "3 - Encerrar\n"
            "Escolha uma opção: "
        )
    except ValueError:
        print("=================================\n Nome inválido, tente novamente.\n=================================")
        continue
        
    if comando == ("1"):   # Adiciona pessoas à fila.
        try:
            for i in range(int(input("Digite a quantidade de pessoas que voce quer adicionar: "))):
                print("Fila atual: ", lista)
                lista.append(input("Ola seja bem vindo, digite seu nome: "))
        except ValueError:
            print("=================================\n Comando invalido, tente novamente.\n================================= ")  
            continue  
            
    elif comando == ("2"):   # Chama o primeiro da fila.
        try:
            pessoach = lista.pop(0)
            print(pessoach, " é a sua vez, por favor venha. ")
        except IndexError:     
            print("================================\n Lista de atendimento vazia.\n================================")
            continue
            
    elif comando == ("3"):  # Encerra o sistema.
        break
    else:
        print("=================================\n Comando errado, tente novamente\n=================================")
