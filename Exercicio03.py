num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
num4 = int(input("Digite um numero: "))
num5 = int(input("Digite um numero: "))

numeros = [num1,num2,num3,num4,num5]
filtrando = filter(lambda x: 'n' in x >10 ,[numeros])
list(filtrando(numeros))
