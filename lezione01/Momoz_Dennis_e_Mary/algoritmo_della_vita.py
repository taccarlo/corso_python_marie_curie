#algoritmo della vita
#riquadro giallo

def Funzione_1:
    print("La persona è nata!")
    print("La persona segue le elementari e le medie.")
    n_bocciature = 0
    anno_superiori = 0
    N = 0
    print(f"Seguo il {N} anno delle superiori.")
    anno_superiori = anno_superiori+1
    while True:
        bocciatura = int(input("Sarò bocciato? 0=sì 1=no"))
        if bocciatura == 0:
            n_bocciature = n_bocciature+1
            if n_bocciature>3:
                print("Meglio se vado a lavorare.")
        else:
            anno_superiori = anno_superiori+1
            if anno_superiori ==5:
                print("Finalmente vado a lavorare")
        
        
        
        
    
