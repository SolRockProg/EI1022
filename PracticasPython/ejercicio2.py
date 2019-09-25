lista=[]
while True:
    a=int(input("Introduce un numero: "))
    if a<0:
        break
    lista.append(a)
lista.sort()
for elem in lista:
    print(elem)