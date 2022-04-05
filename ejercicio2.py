
sexo = str(input("Digite 'mujer' si es mujer o digite 'hombre' si es hombre "))
edad = int(input("Digite la edad "))
if sexo == "mujer" and edad >54:
    print("Ya puede jubilarse")
elif sexo == "hombre" and edad >59:
    print("Ya puede jubilarse")
else:
    print("No puede jubilarse")