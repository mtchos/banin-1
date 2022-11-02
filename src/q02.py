print("Brenda Pan Teixeira")
print("Matheus Silva e Sousa")
print("Questao 2")

LMin = int(input("Digite um valor maior que 0: "))
while LMin <= 0:
    LMin = int(input("LMin deve ser um valor maior que 0: "))

LMax = int(input(f"Digite um valor maior que LMin ({LMin}): "))
while LMax <= LMin:
    LMax = int(input(f"LMax deve ser um valor maior que LMin ({LMin}): "))

X = int(input("Digite um valor diferente de zero: "))
while X == 0:
    X = int(input("X deve ser diferente de zero: "))

lista = []
valor_digitado = 1
soma = 0

while valor_digitado != 0:
    valor_digitado = int(input())
    esta_na_faixa = valor_digitado >= LMin and valor_digitado <= LMax
    divisivel_por_x = valor_digitado % X == 0
    esta_na_lista = False
    for valor in lista:
        if valor == valor_digitado:
            esta_na_lista = True

    if esta_na_faixa and divisivel_por_x and esta_na_lista == False:
        soma += valor_digitado
        lista.append(valor_digitado)

media = 0
if len(lista) != 0:
    media = soma / len(lista)

print(lista)
print(len(lista))
print(soma)
print(media)
