# 1. Elaborar um programa Python para somar dois números.
def obterNumeroReal(msg):
    num = input(msg)
    try:
        num = float(num)
        return num
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
        return obterNumeroReal(msg)

def somarDoisNumeros():
    n1 = obterNumeroReal("Informe o 1º Número: ")
    n2 = obterNumeroReal("Informe o 2º Número: ")
    return n1 + n2

print("Este algoritmo está programado para receber 2 números (sejam eles Reais)")
print("O resultado da soma é:", somarDoisNumeros())