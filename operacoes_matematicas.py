# Recebendo os números e convertendo para float (permite decimais)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Recebendo a operação
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Lógica condicional para decidir o cálculo
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    # Uma pequena validação para não dividir por zero!
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero não permitida."
else:
    resultado = "Operação inválida!"

print(f"\nO resultado da operação é: {resultado}")

