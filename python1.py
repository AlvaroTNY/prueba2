lista = list(["mano","manzana","pera"])
for i in lista:
  print(i)


def suma(*num):
  return sum(num)

print(suma(2,3,4,5,67,79))
