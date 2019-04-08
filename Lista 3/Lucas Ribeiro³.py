'''#EXERCÍCIO 1
nota = float(input("Digite uma nota (0-10): "))

while (nota < 0 or nota > 10):
    print("Valor inválido!")
    nota = float(input("Digite uma nota (0-10): "))

else:
    print("Valor informado foi %.1f."%nota)'''




'''#EXERCÍCIO 2
user = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")

while (user == senha):
    print("A senha não pode ser igual ao usuário!")
    user = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")

else:
    print("Sucesso!")'''




'''#EXERCÍCIO 3

popA = 80000
popB = 200000
ano = 0

while(popA <= popB):
    popA = 3/100 * popA + popA
    popB = 1.5/100 * popB + popB
    ano += 1

    print("Será necessário %d anos para A superar ou igualar B"%ano)'''




'''#EXERCÍCIO 4
fibonacci = [1,1]
i = 0
numero = int(input("Digite um número: "))
a = numero - 1
anteA = a - 1
while (numero >= 1):
    print("Sequência de fibonacci: %d, %d"%a %anteA)'''



'''#EXERCÍCIO 5
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 < n2:
    n1, n2 = n2, n1
r1, mdc = n1 % n2, n2

while r1 !=0:
    r1, mdc = mdc % 1, r1

print("O MDC de %d e %d é %d"%(n1,n2,mdc))'''

    
