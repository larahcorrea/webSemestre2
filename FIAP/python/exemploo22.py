v1 = float(input("digite o raio, altura ou lado  "))
v2 = float(input("digite o raio, altura ou lado  "))

menu = print("1 – Triângulo 2 – Quadrado 3 – Retângulo 4 – Círculo 5 – Fim de processo ")

area = v1 * v2
circulo = 3,14 * v1 * v2
 
o = int(input("digite o número da operação  "))

if o == 1 or 0 == 2 or o == 3 :
    print( "A resposta é  ",area )
elif o == 4:
    print("A resposta é  ", circulo)
else:
    print()
    


 
