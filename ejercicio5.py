

burger_sencilla  = int = 20
burger_doble = int  = 25
burger_triple = int = 28
forma_de_pago = float (input("Digite 1 si paga con efectivo, digite 2 si paga con tarjeta "))
if forma_de_pago == 1:
    N1 = float (input("Digite cu1antas hamburguesas sencillas quiere comprar, si no quiere comprar digite 0 : "))
    N2 = float (input("Digite cuantas hamburguesas doble quiere comprar, si no quiere comprar digite 0 : "))
    N3 = float (input("Digite cuantas hamburguesas triples quiere comprar, si no quiere comprar digite 0 : "))
    total = N1*burger_sencilla + N2*burger_doble + N3*burger_triple
    print(f"Total a pagar es de {total}")
elif forma_de_pago == 2:
    N1 = float (input("Digite cuantas hamburguesas sencillas quiere comprar, si no quiere comprar digite 0 : "))
    N2 = float (input("Digite cuantas hamburguesas doble quiere comprar, si no quiere comprar digite 0 : "))
    N3 = float (input("Digite cuantas hamburguesas triples quiere comprar, si no quiere comprar digite 0 : "))
    calculo = (N1*burger_sencilla + N2*burger_doble + N3*burger_triple)*5/100
    total = (N1*burger_sencilla + N2*burger_doble + N3*burger_triple)+calculo
    print(f"Total a pagar es de {total}")