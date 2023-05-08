
def incipit():
    '''
    In questa funzione chiediamo il numero,
    ritorniamo True o False se riusciamo già a diventare migliori amici oppure no
    '''
    print("Componi il numero della persona chiamata")
    risp =int(input("E' in casa? 0=no 1=sì "))
    if(risp == 0):
        print("Lascia un messaggio e aspetta di essere richiamato")
    risp =int(input("Ti va di mangiare qualcosa insieme? 0=no 1=sì "))
    if(risp == 0):
        return False
    else:
        print("Mangiate qualcosa insieme")
        return True

def offertaBevanda():
    '''
    in questa funzione offro da bere, se non accettano chiamo offertaAttivita()
    '''

def offertaAttivita():
    print("Allora svaghiamoci un po'...")
    '''
    In questa funzione chiediamo per 6 volte al massimo se ci va di fare qualcosa
    '''
    
   
risp1 = incipit()
if(risp1==False):
    offertaBevanda()

print('"Siete diventati migliori amici! Ora hai una persona in più a cui poter rompere le palle in caso di bisogno e viceversa."')


