
import math


figura = int(input("Digite 1 si quiere calcular el area del triángulo, 2 para el area del circulo, 3 para el area del rectángulo y 4 para el area de el hexágono "))
if figura == 1:
    b = int(input("Digite la Base del triángulo en metros "))
    h = int(input("Digite la Altura del triángulo en metros "))
    area = b*h/2
    print(f"El area del triángulo es {area} m²")
elif figura == 2:
    R = int(input("Digite el Radio del circulo en cm  "))
    area = math.pi*R**2
    print(f"El area del circulo es {area} cm²")
elif figura == 3:
    b = int(input("Digite la Base del rectángulo en cm "))
    h = int(input("Digite la Altura del rectángulo en cm "))
    area = b*h
    print(f"El area del rectángulo es {area} cm²")
elif figura == 4:
    a = float(input("Digite cuanto mide el apotema del hexágono en cm "))
    l = float(input("Digite cuanto mide el lado del hexágono en cm "))
    P = l*6
    area = P*a/2
    print(f"El area del héxanogo es de {area} cm²")