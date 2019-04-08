'''#EXERCÍCIO 1
import random

lista = []

maior = 0

menor = 100

for i in range(10):
    n = random.randint(1,100)
    lista.append(n)

    if n < menor:
        menor = n

    if n > maior:
        maior= n

lista.sort()
print(lista)
print("Menor número: %d \nMaior número: %d"%(menor, maior))




#EXERCÍCIO 2
import random

lista = []

impar = []

par = []

for i in range(20):
    n = random.randint(1,100)
    lista.append(n)

    if n % 2 == 0:
        par.append(n)

    if n %2 == 1:
        impar.append(n)

lista.sort()

print(lista)
print("Lista impar",impar)
print("Lista par",par)




#EXERCÍCIO 3
import random

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    lista1.sort()
    lista1.append(random.randint(1,100))

    lista2.sort()
    lista2.append(random.randint(1,100))

    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista1,"\n")
print(lista2,"\n")
print(lista3)'''




'''#EXERCÍCIO 4
texto = "The Python Software Foundation and the global Python \
community welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each other live up \
to these principles. We want our community to be more diverse: whoever you are, and \
whatever your background, we welcome you."

palavra = texto.split()

#print(palavra)

palavraPython = []

for p in palavra:

    if py[0] in "python" or py[-1] in "python":
        
        palavraPython.append(py)

print("\n",palavraPython,"\n")'''



#EXERCÍCIO 5
texto = "The Python Software Foundation and the global Python \
community welcome and encourage participation by everyone. Our community is based on \
mutual respect, tolerance, and encouragement, and we are working to help each other live up \
to these principles. We want our community to be more diverse: whoever you are, and \
whatever your background, we welcome you."

palavra = texto.split()

palavra_python = []

for p in palavra:
    py = p.lower()

    if py[0] in "python" and len(py) > 4:
        palavra_python.append(py)
        
print(palavra_python)
    
