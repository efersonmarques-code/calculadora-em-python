operacao = input("Qual operacao quer fazer? (+, -, *, /):")

# somar
if operacao == "+":
    numero1 = int(input("Digite o primeiro numero:"))
    numero2 =  int(input("Digite o segundo numero:"))
    print(f"A soma e: {numero1 + numero2}")

# subtração
elif operacao == "-":
    numero1 = int(input("Digite o primeiro numero:"))
    numero2 = int(input("Digite o segundo  numero:"))
    print(f"A subtração e: {numero1 - numero2}")

# multiplicação
elif operacao == "*":
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))
    print(f"A multiplicação e: {numero1 * numero2}")

# divisão
elif operacao == "/":
    numero1 = float(input("Digite o primeiro número:"))
    numero2 = float(input("Digite o segundo número:"))
    
  try:
        print(f"A divisão e: {numero1 / numero2}")
    except ZeroDivisionError:
  
        print("Erro não e possível dividir por zero!")
        
else:
    print("Operação inválida!")