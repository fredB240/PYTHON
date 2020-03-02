"""
https://interstices.info/les-algorithmes-de-tri/

procedure triBulle(entier[] tab)
  entier i, k;
  entier tmp;
  pour (i de N à 2 en décrémentant de 1) faire
    pour (k de 1 à i-1 en incrémentant de 1) faire
      si (tab[k] > tab[k+1]) alors
        tmp <- tab[k];
        tab[k] <- tab[k+1];
        tab[k+1] <- tmp;
      fin si
    fin pour
  fin pour
fin procedure
"""

def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n,1,-1):
        for k in range(0, i-1,1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[k] > tab[k+1] :
                tab[k], tab[k+1] = tab[k+1], tab[k]

# Programme principal pour tester le code ci-dessus
#tab = [98, 22, 15, 32, 2, 74, 63, 70]
#import random
#tab = random.sample(range(0, 100), 10)
#print(tab)
tab = [4,2,5,1,6,3] 
tri_bulle(tab)
 
print ("Le tableau trié par bulle est:")
for i in range(len(tab)):
    print ("%d" %tab[i])


