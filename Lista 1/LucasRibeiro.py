#EXERCÍCIO 1
num1 = input("Digite o primeiro número:")
num2 = input("Digite o segundo número:")

soma = int(num1) + int(num2)

print("Resultado da soma =",soma)





#EXERCÍCIO 2
numMetro = input("Insira o valor em metros:")

conversao = float(numMetro) * 1000

print("Valor inserido convertido para milímetros: ", conversao)





#EXERCÍCIO 3
dia = input("Digite a quantidade de dias:")
horas = input("Digite a quantidade de horas:")
minutos = input("Digite a quantiade de minutos:")
segundos = input("Digite a quantidade de segundos:")

total = int(segundos) + int(minutos)*60 + int(horas)*3600 + int(dia)*86400

print("Total da somatória em segundos = ",total)





#EXERCÍCIO 4
salario = input("Digite o valor do salário:")
porcent = input("Insira o valor da porcentagem de aumento:")

reajuste = float(salario) + float(porcent)/100 * float(salario)

print("Valor reajustado do salário = ", reajuste)





#EXERCÍCIO 5
preco = input("Insira o preço da mercadoria:")
desconto = input("Digite a porcentagem de desconto:")

total = float(preco) - float(desconto)/100 * float(preco)

print("Valor do desconto: ",desconto)
print("Valor a ser pago: ",total)





#EXERCÍCIO 6
velMedia = input("Digite a velocidade média para a viagem:")
dist = input("Digite a distância total a ser percorrida:")

tempo = float(dist)/float(velMedia)

print("O tempo que será gasto na viagem é: ",tempo)





#EXERCÍCIO 7
tempC = input("Digite a temperatura em graus Celsius:")

tempF = 9* float(tempC)/5 + 32

print("A temepratura digitada, em graus Fahrenheit é:´",tempF)





#EXERCÍCIO 8
tempF = input("Digite a temperatura em graus Fahrenheit:")

tempC = float(tempF)-32/1.8

print("Temperatura digitada, em graus Celsius: ",tempC)





#EXERCÍCIO 9
kmPerc = input("Digite a quantidade de quilômetros percorridos:")
diaAlug = input("Por quantos dias o carro foi alugado?")

totalPag = float(kmPerc) * 0.15 + int(diaAlug) * 60

print("Total a pagar pela locação: ",totalPag)





#EXERCÍCIO 10
porDia = input("Quantos cigarro você fuma por dia? ");
anosFuma = input("Quantos anos já fumou? ");

vidaDia = int(porDia) * 10
vidaAno = (vidaDia * 365) * int(anosFuma)
totalDia = vidaAno/24

print("Total de dias de vida perdido: ",totalDia)





#EXERCÍCIO 11
num = str(pow(2,1000000))
print("2^1000000 possui %d dígitos" %len(num))
