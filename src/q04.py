import random

print("Brenda Pan Teixeira")
print("Matheus Silva e Sousa")
print("Questao 4")

tipo = int(input("[1] - Para ser o adivinhador\n[2] - Para ser o sorteador\n"))
while tipo != 1 and tipo != 2:
    tipo = int(input("[1] - Para ser o adivinhador\n[2] - Para ser o sorteador\n"))

LMin = int(input("Digite o valor mínimo: "))

LMax = int(input("Digite o valor máximo: "))
while LMax <= LMin + 100:
    LMax = int(input("Digite o valor máximo: "))


def humano_adivinhador():
    segredo = random.randint(LMin, LMax + 1)
    palpites = []
    tentativas = 0
    tentativa_atual = int(input("Tente a sorte: "))
    while tentativa_atual != segredo:
        if tentativa_atual > segredo:
            print("Você errou. O valor a ser adivinhado é menor!")
        else:
            print("Você errou. O valor a ser adivinhado é maior!")
        palpites.append(tentativa_atual)
        tentativas += 1
        tentativa_atual = int(input("Tente a sorte novamente: "))
    print("Você acertou!")
    return [palpites, tentativas]


def humano_sorteador():
    segredo = int(input("Digite o valor a ser adivinhado: "))
    palpites = []
    tentativas = 0
    limite_min_palpite = LMin
    limite_max_palpite = LMax
    tentativa_atual = random.randint(limite_min_palpite, limite_max_palpite + 1)
    while tentativa_atual != segredo:
        if tentativa_atual > segredo:
            limite_max_palpite = tentativa_atual - 1
        else:
            limite_min_palpite = tentativa_atual + 1
        palpites.append(tentativa_atual)
        tentativas += 1
        tentativa_atual = random.randint(limite_min_palpite, limite_max_palpite + 1)
    return [palpites, tentativas]


palpites, tentativas = None, None
if tipo == 1:
    palpites, tentativas = humano_adivinhador()
elif tipo == 2:
    palpites, tentativas = humano_sorteador()

print(f"Palpites: {palpites}")
print(f"Tentativas: {tentativas}")
