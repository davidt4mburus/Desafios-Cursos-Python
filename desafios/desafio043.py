peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO normal")
elif 18.5 <= imc < 25:
    print("PARABÉNS! Você está no PESO IDEAL")
elif 25 <= imc < 30:
    print("Você está ACIMA DO PESO normal")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE")
elif imc >= 40:
    print("CUIDADO! Você está em OBESIDADE MORBIDA!")