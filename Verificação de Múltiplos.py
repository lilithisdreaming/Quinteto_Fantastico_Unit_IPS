#Verificador de Multiplos, informa se X numero é multiplo de 3 e de 5, de 3, de 5 ou de nenhum
#Comandos obrigatorios utilizados: input(), if, elif, else, print()

numero =int(input("Insira um número inteiro: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 3 e 5.")
elif numero % 3 == 0:
    print(f"O número {numero} é múltiplo de 3, mas não de 5.")
elif numero % 5 == 0:
    print(f"O número {numero} é múltiplo de 5, mas não de 3.")
else:
    print(f"O número {numero} não é múltiplo de 3 nem de 5.")
