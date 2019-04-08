#EXERCÍCIO 1
lado1 = input("Digite a tamanho lado do triângulo:")
lado2 = input("Digite a tamanho lado do triângulo:")
lado3 = input("Digite a tamanho lado do triângulo:")

if lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado3 != lado1:
    print('Triângulo isóceles!')
    
elif lado1 == lado2 and lado2 == lado3:
    print('Triângulo equilátero!')
    
else:
    print('Triângulo escaleno!')




#EXERCÍCIO 2
ano = int(input("Digite um ano para saber se é bissexto ou não:"))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ano digitado é bissexto!')

else:
    print('O ano digitado não é bissexto!')


    

#EXERCÍCIO 3

pesoPeixe = float(input("Digite o peso dos peixes:"))
multa = 4
if pesoPeixe > 50:
    excesso = pesoPeixe - 50
    multa = multa * excesso

    print("Peso excedido em .",excesso,"kg.","Multa de ",multa,"R$")

else:
    print("Parabéns, nenhuma multa!")




#EXERCÍCIO 4
num1 = input("Digite um número:")
num2 = input("Digite outro número:")
num3 = input("Digite o último número:")

if num1 > num2 or num1 > num3:
    print("O primeiro número é o maior!")

elif num2 > num1 or num2 > num3:
    print("O segundo número é o maior!")

else:
    print("O terceiro número é o maior!")




#EXERCÍCIO 5
num1 = input("Digite um número:")
num2 = input("Digite outro número:")
num3 = input("Digite o último número:")

if num1 > num3 and num3 > num2:
    print("O primeiro é o maior e o segundo é o menor.")

elif num1 > num2 and num3 < num1:
    print("O primeiro é o maior e o terceiro é o menor.")

elif num2 > num3 and num1 < num2:
    print("O segundo é o maior e o primeiro é o menor.")

elif num2 > num3 and num3 < num1:
    print("O segundo é o maior e o terceiro é o menor.")

elif num3 > num1 and num2 < num1:
    print("O terceiro é o maior e o segundo é o menor.")

elif num3 > num1 and num1 < num2:
    print("O terceiro é o maior e o primeiro é o menor.")




#EXERCÍCIO 6
salario = float(input("Digite o valor que ganha por hora: "))
nHoras = int(input("Digite o número de horas trabalhadas no mês: "))

salBruto = salario * nHoras

impRenda = 11/100 * salBruto

inss = 8/100 * salBruto

sindicato = 5/100 * salBruto

salLiquido = salBruto - impRenda - inss - sindicato

print("SALÁRIO BRUTO: ",salBruto, "desconto do imposto de renda: ",impRenda,
      "desconto do INSS: ",inss, "desconto do sindicato: ",sindicato,
      "SALÁRIO LÍQUIDO: ",salLiquido)




#EXERCÍCIO 7
lata = 18
preco = 80
tamanho = int(input("Digite o tamanho a ser pintado, em metros quadrados: "))

if tamanho %54 != 0 and tamanho <= 54:
    print("Uma lata. preço total: 80.00.")

else:
    totalLata = tamanho / 54
    precoTotal = totalLata * preco

    print("Total de latas de tinta:",round(totalLata), "Preço total:",round(precoTotal, 2))




    
                
