'''
6) desenvolver um programa que multiplique sucessivamente um número por 3 antes que exceda 250
'''

n = int(input("Informe um número menor ou igual a 50: "))
if ( n <= 50 ):
 while ( n < 250 ):
     print(n)
     n = n * 3

 else:
     print(f"{n} não é menor ou igul a 50")