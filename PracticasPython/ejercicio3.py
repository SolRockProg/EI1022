d={"Manolo":3, "Juan": 4, "Fran": 64}
nombre=input("Dame un nombre: ")
if not nombre in d:
    print("No esta en el diccionario")
else:
    print("Su edad es {}".format(d[nombre]))