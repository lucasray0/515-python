# def somar(num1, num2):
#     return num1 + num2

# num1 = float(input("primeiro numero: "))
# num2 = float(input("segundo numero: "))

# print(somar(num1, num2))


# quadrado = lambda numero : numero ** 2
# numero = float(input("escreva o numero: "))

# print(quadrado(numero))


# def maior_de_todos(numero):
#     return (max(numero))

# lista = []
# for i in range(5):
#     numero = float(input("digite o numero: "))
#     lista.append(numero)


# print(maior_de_todos(lista))


# lista = []
# for i in range(5):
#     numero = float(input("escreva o numero: "))
#     lista.append(numero)

# mult = list(map(lambda numero : numero * 2, lista))


# print(mult)



# verificar = lambda numero : 'é par' if numero % 2 == 0 else "é impar"

# numero = float(input("escreva numero: "))

# print(verificar(numero))


lista = []
for i in range(4):
    numero = float(input("escreva numero: "))
    lista.append(numero)

def listamedia (numeros):
    return sum(numeros) / len(numeros)



print(listamedia(lista))