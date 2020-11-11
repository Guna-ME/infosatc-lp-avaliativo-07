num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
num4 = int(input("Digite um numero: "))
num5 = int(input("Digite um numero: "))
num6 = int(input("Digite um numero: "))
num7 = int(input("Digite um numero: "))
num8 = int(input("Digite um numero: "))
num9 = int(input("Digite um numero: "))
num10 = int(input("Digite um numero: "))

numeros = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

par = filter(lambda x: '%2==0' in x, print("é par: ",[numeros]))  
impar = filter(lambda x: '%!=0' in x, print("é ímpar: ",[numeros]))