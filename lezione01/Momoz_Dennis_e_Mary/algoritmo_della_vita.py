
#algoritmo della vita
#riquadro giallo

def Funzione_1():
    print("La persona è nata!")
    print("La persona segue le elementari e le medie.")
    n_bocciature = 0
    anno_superiori = 0
    while True:
        N = 1
        print(f"Seguo il {N} anno delle superiori.")
        anno_superiori = anno_superiori+1
        bocciatura = int(input("Sarò bocciato? 0=sì 1=no"))
        if bocciatura==0:
            n_bocciature = n_bocciature+1
            if n_bocciature>3:
                print("Meglio se vado a lavorare.")
        else:
            anno_superiori = anno_superiori+1
            if anno_superiori==5:
                print("Finalmente vado a lavorare")
        N = N+1
    return Funzione_2()

def Funzione_2:
print(Anni di lavoro=0)
while Anni di lavoro < 20:
    Anni di lavoro = Anni di lavoro + 1
    print("L'anno lavorativo si conclude")
    infortunio = int(input("Subisci un infortunio debilitante? 0=sì 1=no"))
    if infortunio==0:
        print("vai in pensione")
    else:
        print("ultimi anni di lavoro")
    return Funzione_3


def Funzione_3:
promozioni = int(input("Quante promozioni sono state ottenute nel corso della carriera?")
if promozioni >3:
    print("capo di azienda")
print("pensione")
return       
        
        
