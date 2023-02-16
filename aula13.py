# O IMC é calculado dividindo o peso (em kg)
# pela altura ao quadrado (em m), de acordo
# com a seguinte fórmula: IMC = peso / (altura x altura).

nome = "Ellias Santos"
altura = 1.70
peso = 50
imc = peso / altura ** 2

# f-strings
linha1 = f"{nome} tem {altura:.2f} de altura" #.2f -> 2 casas decimais
linha2 = f"pesa {peso} quilos e seu IMC é:"
linha3 = f"{imc:.2f}"

print(linha1)
print(linha2)
print(linha3)


# print(nome, "tem", altura, "de altura,")
# print("pesa", peso, "quilos e seu IMC é")
# print(imc)

# Ellias Santos tem 1.70 de altura,
# pesa 50 quilos e seu IMC é 
# 17.301038062283737