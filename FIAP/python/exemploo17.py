peso = float(input("digite peso  "))
altura = float(input("digite altura  "))
sexo = input("digite M/F  ")
  
imc = peso/ (altura * altura)

if sexo == "M":
    if (imc < 20):
         print("Peso abaixo do ideal!")
    elif (imc < 25):
        print("Peso ideal!")
    else: 
        print("Peso acima do ideal!")
else:
    if (imc <19 ):
        print("Peso abaixo do ideal!")
    elif (imc < 24):
        print("Peso ideal!")
    else:
        print("Peso acima do ideal!")


