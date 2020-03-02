"""
procedure triSelection(entier[] tab)
  entier i, k;
  entier min;
  entier tmp;
  pour (i de 1 à N-1 en incrémentant de 1) faire

    /* recherche du numero du minimum */

    min <- i;
    pour (k de i+1 à N en incrémentant de 1) faire
      si (tab[k] < tab[min]) alors
        min <- k;
      fin si
    fin pour

    /* echange des valeurs entre la case courante et le minimum */

    tmp <- tab[i];
    tab[i] <- tab[min];
    tab[min] <- tmp;
  fin pour
fin procedure
"""

def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for k in range(i+1, len(tab)):
           if  tab[k] < tab[min]:
               min = k
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab

# Programme principal pour tester le code ci-dessus
tab = [4,2,5,1]
 
tri_selection(tab)
 
print ("Le tableau trié par selection est:")
for i in range(len(tab)):
    print ("%d" %tab[i])
