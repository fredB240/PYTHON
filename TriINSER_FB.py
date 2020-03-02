"""
procedure triInsertion(entier[] tab)
  entier i, k;
  entier tmp;
  entier k;
  pour (i de 2 à N en incrémentant de 1) faire
    tmp <- tab[i];
    k <- i; 
    tant que (k > 1 et tab[k - 1] > tmp) faire
      tab[k] <- tab[k - 1];
      k <- k - 1;
    fin tant que
  tab[k] <- tmp;
  fin pour
fin procedure
"""

# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        tmp = tab[i] 
        k = i
        while k > 0 and tab[k-1] > tmp : 
                memoire = tab[k-1]
                tab[k] = memoire
                k -= 1
        tab[k] = tmp

# Programme principal pour tester le code ci-dessus
tab = [4,2,5,1]
print(len(tab))
tri_insertion(tab) 
print ("Le tableau trié par insertion est:")
for i in range(len(tab)): 
    print ("% d" % tab[i])

