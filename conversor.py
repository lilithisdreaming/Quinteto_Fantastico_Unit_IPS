# Programa que converte um valor em horas para minutos e segundos.
# A conversão é feita multiplicando horas por 60 (minutos) e minutos por 60 (segundos).
# Utiliza input() para entrada e print() para exibir o resultado.

horas = float(input("Digite um valor em horas: "))
minutos = horas *60
segundos = minutos*60
print(f"O valor dado em {horas} horas é igual à {minutos} minutos ou {segundos} segundos. ")
