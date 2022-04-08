lista = [2,5,2,8,5]

print(len(lista))
print(lista[3])
serie = range(0,10)

dias = ("S","T","Q","Q","S","S","D")

print(len(dias))

p1 = (3,9)
p2 = (4,8)
p3 = (2,6)
line = [p1,p2,p3]

print(line)

f1 = ("Safira",2)
f2 = ("Branca",8)

pets = [f1,f2]

print(pets)

print(pets[0][0])

palavras = []
palavras.append("relogio")
palavras.append("perfume")
coisas = tuple(palavras)
print(coisas)
outra = list(coisas)
print(outra)

inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]

print(pares)