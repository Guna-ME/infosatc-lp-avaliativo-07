def abcd(media):
    if media<=5.0 and media>=0:
        letra="D"
    elif media<=7.0 and media>5.0:
        letra="C"
    elif media<9.0 and media>7.0:
        letra="B"
    elif media>=9 and media<=10:
        letra="A"
    return letra

for x in range (0,10):
    nota1 = float(input("Insira a primeira nota:"))
    nota2 = float(input("Insira a segunda nota:"))
    media = mediaP(nota1,nota2)
    conceito = abcd(media)
    print("O aluno possui média igual a: ",media)
    print("O aluno possui conceito igual a: ",conceito)
