print("Brenda Pan Teixeira")
print("Matheus Silva e Sousa")
print("Questao 3")

codigos = [16, 23, 27, 34]
preco_unitario_varejo = [14.35, 35.12, 19.35, 63.40]
preco_unitario_atacado = [12.93, 29.85, 16.76, 58.25]
quantidade_minima_atacado = [50, 100, 70, 40]

numero_vendas = int(input("Digite o número de vendas realizadas: "))
while numero_vendas <= 0:
    numero_vendas = int(input("Digite um número de vendas maior que zero: "))

total_varejo = 0
total_atacado = 0

for venda in range(numero_vendas):
    codigo, quantidade_venda = map(int, input().split())
    if codigo in codigos:
        indice = codigos.index(codigo)
        if quantidade_venda >= quantidade_minima_atacado[indice]:
            total_atacado += preco_unitario_atacado[indice] * quantidade_venda
        else:
            total_varejo += preco_unitario_varejo[indice] * quantidade_venda
    else:
        print("Código inválido")

total = total_varejo + total_atacado

print(f"Total de Vendas do Grupo Varejo: R$ {total_varejo:.2f}")
print(f"Total de Vendas do Grupo Atacado: R$ {total_atacado:.2f}")
print(f"Vendas Totais: R$ {total:.2f}")
