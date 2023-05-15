def funzione1():
    anno_s = 1 #anno_s = anno superiori
    bocciature = 0 #bocciature = numero bocciature
    while anno_superiori<=5:
        print ("seguo il", anno_s,"° delle superiori")
        domanda_b = int(input("sei stato bocciato?\n( 1 se SI', 0 se NO )")) #domanda_b = input che serve per capire se è stato bocciato oppure no
        if domanda_b == 0:
            anno_s = anno_s +1
        else:
            bocciature = bocciature+1
        elif bocciature>3:
            return funzione2
    
def funzione2():
    n = 0
    while n>=20:
        n=n+1
        print("Anno di servizio", n)
    infortunio = int(input("Infortunio debilitante? (1 se si, 0 se no)"))
    if infortunio== 1:
        return 'pensione'
    else:
        return funzione3()
    
    
def funzione3():
    return 'pensione'


print("La persona è nata")
