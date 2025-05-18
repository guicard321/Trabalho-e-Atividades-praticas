saida = ''

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0."
    return a / b

def calculadora(a, b, operacao):
    if operacao in ("+", "soma", "adição", "adicao"):
        resultado = adicao(a, b)
    elif operacao in ("-", "subtração", "subtracao"):
        resultado = subtracao(a, b)
    elif operacao in ("*", "multiplicação", "multiplicacao"):
        resultado = multiplicacao(a, b)
    elif operacao in ("/", "divisão", "divisao"):
        resultado = divisao(a, b)
    else:
        resultado = "Operação inválida."
    return resultado

while saida.lower() != "n":
    while True:
        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Por favor, digite apenas números válidos. (use '.' para Decimal) \nTente novamente.") 

    while True:
        operacao = input("Escolha a operação desejada: \n(+, -, *, / ou 'soma/adição', subtração, multiplicação, divisão): ").strip().lower()
        resultado = calculadora(a, b, operacao)
        if resultado == "Operação inválida.":
            print("Operação inválida. Tente novamente.")
        else:
            break

    print("Resultado da operação: ", resultado)
    saida = input("Deseja continuar? (S/N): ").strip().lower()
    
    while saida not in ("s", "n"):
        print("Opção inválida. Digite 'S' para continuar ou 'N' para sair.")
        saida = input("Deseja continuar? (S/N): ").strip().lower()

print("Calculadora encerrada.")