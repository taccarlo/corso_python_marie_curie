




def funzione1():
    print("La persona è nata!")
    print("La persona segtue le elementari e le medie")
    n_bocciature=0
    anno_superiori=0
    n_bocciature=0
    while True:
        print(f'segue il {anno_superiori} anno delle superiori')
        anno_superiori+=1
        bocciature=int(input("Sei stato bocciato, se sì digita 1, altrimenti 0?")
        if bocciature == 1:
            n_bocciature+=1
            if n_bocciature > 3:
                return funzione2
        else:
            if anno_superiori == 5:
                return funzione2
                
               
               
               
def funzione2:
    lavoro=0
    
    while lavoro<=20:
        lavoro=lavoro+1
        print(lavoro, "anni di lavoro")
    infortunio=int(input("presenza di infortunio delibitante? se si digita 1 altrimenti digita 0"))
    if infortunio==1:
        return "pensione" 
    else:
        return funzione3

