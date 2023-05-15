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
    return funzione3()
    
def funzione3():
    return 'pensione'


print("La persona è nata")
