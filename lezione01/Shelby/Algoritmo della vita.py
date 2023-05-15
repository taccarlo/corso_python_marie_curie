

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