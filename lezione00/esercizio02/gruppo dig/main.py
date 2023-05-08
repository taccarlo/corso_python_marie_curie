







def parte_2 :
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
        return no
    