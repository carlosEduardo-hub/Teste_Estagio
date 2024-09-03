def verificar_letra_a(texto):
    contador = texto.lower().count('a')

    if contador > 0:
        print(f"A letra 'a' ocorre {contador} veza(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")


string = input("Informe uma string: ")
verificar_letra_a(string)
