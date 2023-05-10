
def parte1():
    while True:
        ris=int(input("componi il numero di telefono della persona \nè in casa? Se si digita 1, altrimenti 0"))
        if ris==1:
            ris=int(input("Ti va di mangiare qualcosa insieme? Se si digita 1, altrimenti 0"))
            if ris==1:
                print("mangiate qualcosa insieme")
                return "Siete diventati amici. Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa"
                
            else:
                return parte2()
                    
                    
def parte2():
    risposta_3 = input("e di bere qualcosa? Se si digita 1, altrimenti 0 ")
    if risposta_3 == 1 :
        risposta_3a = int(input("scegli: \n1_ tè \n2_caffè \n3_cioccolata"))
        if risposta_3a == 1:
            return ("FATEVI 'STO TE' -> \nSiete diventati amici. Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa ")
        elif risposta_3a == 2:
            return ("FATEVI 'STO CAFFE' -> \nSiete diventati amici. Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa ")
        elif risposta_3a == 3:
            return ("FATEVI 'STA CIOCCOLATA -> \nSiete diventati amici. Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa ")
    else:
        return parte3()       


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


print(parte1())
    