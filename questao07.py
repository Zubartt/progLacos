'''
programa que mostre todos os números divisíveis por 4 de 0 a 200.
'''

cont = 1
while ( cont < 200 ):
    div4 = cont % 4
    if ( div4 == 0 ):
        print(f"{cont} é divisível por 4")

    cont = cont + 1
