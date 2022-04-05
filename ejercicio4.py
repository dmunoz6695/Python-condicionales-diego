sueldo_neto = int(input("Digite su sueldo neto "))
venta = int(input("Digite cuanto vendió "))
if venta >2000 and venta < 3001:
    calculo = sueldo_neto * 6 / 100
    calculo2 = sueldo_neto + calculo
    print(f"Usted cobrará {calculo2} es decir ganó {calculo} por comisión ")
elif venta >3000 and venta < 5001:
    calculo = sueldo_neto * 18 / 100
    calculo2 = sueldo_neto + calculo
    print(f"Usted cobrará {calculo2} es decir ganó {calculo} por comisión ")
elif venta >5000:
    calculo = sueldo_neto * 12 / 100
    calculo2 = sueldo_neto + calculo
    print(f"Usted cobrará {calculo2} es decir ganó {calculo} por comisión ")
else:
    print(f"Usted cobrará {sueldo_neto} no vendió más de 2000 por ende no tendrá comisión")

