print("Brenda Pan Teixeira")
print("Matheus Silva e Sousa")
print("Questao 1")

segundos = int(input())
horas = int(segundos / 3600)
segundos -= (horas * 3600)
minutos = int(segundos / 60)
segundos -= (minutos * 60)
print("{} horas, {} minutos, {} segundos".format(horas, minutos, segundos))

print("teste")
