
def incipit():
    '''
    In questa funzione chiediamo il numero,
    ritorniamo True o False se riusciamo già a diventare migliori amici oppure no
    '''
    '''
    ...
    '''

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


