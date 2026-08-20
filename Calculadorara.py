operacao = input("Qual operacao quer fazer? (+, -, *, /): ")

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número.")

if operacao in ("+", "-", "*", "/"):
    numero1 = ler_numero("Digite o primeiro numero: ")
    numero2 = ler_numero("Digite o segundo numero: ")

    if operacao == "+":
        print(f"A soma e: {numero1 + numero2}")
    elif operacao == "-":
        print(f"A subtração e: {numero1 - numero2}")
    elif operacao == "*":
        print(f"A multiplicação e: {numero1 * numero2}")
    elif operacao == "/":
        if numero2 == 0:
            print("Erro: não e possível dividir por zero!")
        else:
            print(f"A divisão e: {numero1 / numero2}")
else:
    print("Operação inválida!")