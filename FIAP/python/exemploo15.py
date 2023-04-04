a = int(input("digite a  "))
b = int(input("digite b  "))
c = int(input("digite c  "))
 

if a == b and b == c :
    print ("Triângulo Equilátero!")
elif a != b and b == c or b != a and a == c or c!= b == a:
    print(" Triângulo Isóceles")
elif a < (a +b ) or b < (a+c) or c < ( b+a):
    print ("Triângulo Escaleno")
else:
    print ("Não é um triângulo")
    

