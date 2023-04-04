v1 = int(input("digite o primeiro valor  "))
v2 = int(input("digite o segundo valor  "))
menu = print( "1 – Multiplicação 2 – Adição 3 – Divisão 4 – Subtração 5 – Fim de processo (sair do programa) ")

m = v1 * v2
a = v1 + v2
d = v1 / v2
s = v1 - v2  
 
o = int(input("digite o número da operação  "))

if o == 1 and v1 != 0 and v2 != 0:
    print( m )
elif o == 2:
    print( a )
elif o == 3 and v1 != 0 and v2 != 0:
    print ( d )
elif o == 4:
    print ( s )
else:
    print()
    


 


