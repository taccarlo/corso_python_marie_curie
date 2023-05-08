
def parte1






def parte2():
    risposta_3 = input("E DI BERE QUALCOSA? (sì o no)")
    if risposta_3 == "sì" :
        risposta_3a = int(input("SCEGLI: \n1_ TE' \n2_CAFFE' \n3_CIOCCOLATA?"))
        if risposta_3a == 1:
            return "FATEVI 'STO TE'"
        elif risposta_3a == 2:
            return "FATEVI 'STO CAFFE'"
        elif risposta_3a == 3:
            return "FATEVI 'STA CIOCCOLATA"
    else:
        return "no"       


def parte3():
    n=0
    print("Allora svaghiamoci un po'. Cos'altro ti va di fare?")
    while True:
        ris=int(input("è una cosa che va fare anche a me: se sì digito 1, altrimenti 0"))
        if ris==1:
            print("E facciamolo insieme, dai")
            print("svagatevi un po' insieme")
            break
        else: 
            n+=1
            if n>=6:
                print("scegli fra tutte le opzioni quella che ti appare meno disumana. Fattela piacere")
                print("svagatevi un po' insieme")
                break
    return("Siete diventati amici. Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa")
print(terzaParte())
    