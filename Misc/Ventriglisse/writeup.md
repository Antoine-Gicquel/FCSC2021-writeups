On parse l'image en python. On créé le graphe suivant :
Chaque case est un sommet
Pour chaque case c, il existe une arête (orientée) (c, c') si depuis c on peut glisser et être bloqué en arrivant en c' (en gros, une arête si on peut faire le déplacement c -> c')
-> Dijkstra
