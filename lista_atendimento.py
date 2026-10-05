# Sistema de atendimento interativo.
# Permite adicionar pessoas à fila, chamar o próximo da lista ou encerrar o programa.
# Usa uma lista para armazenar nomes e um loop while para manter o sistema ativo.
# Inclui tratamento de erros com try/except para evitar falhas em entradas inválidas.

lista = []
LIMITE = 15 # Limite MAX de pessoas que podem ser adicionadas por vez à fila.

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
        
    if comando == "1":  # Adiciona pessoas à fila
        try:
            quantidade = int(input(f"Digite a quantidade de pessoas (máx {LIMITE}): "))
            if quantidade > LIMITE:
                print(f"Você só pode adicionar até {LIMITE} pessoas por vez.")
                continue
            for i in range(quantidade):
                nome = input("Digite o nome: ")
                lista.append(nome)
        except ValueError:
            print("Entrada inválida, tente novamente.")
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
