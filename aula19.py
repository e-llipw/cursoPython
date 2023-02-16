primeiroValor = input("Digite um valor: ")
segundoValor = input("Degite outro valor: ")

maior = primeiroValor > segundoValor
menor = primeiroValor < segundoValor
igual = primeiroValor == segundoValor

if maior:
    print(f"{primeiroValor=} é maior do que o {segundoValor=}")
elif menor:
    print(f"{segundoValor=} é maior do que o {primeiroValor=}")
elif igual:
    print(f"Os dois valores são iguais. {primeiroValor=} é igual ao {segundoValor=}")
else:
    print("Valor inválido")