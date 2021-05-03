Idée de résolution :

p et q sont de la forme : a << 1024 + K, avec K de l'ordre de 128 bits.

Donc N = p\*q = a_p \* a_q << 2048 + K' << 1024 + K'', avec K' et K'' les constantes qui sortent lors du développement de p\*q, de taille < 256 bits.

On peut récupérer a_p \* a_q = N >> 2048. En le factorisant, on obtient une seule solution (à permutation près) dont les 2 facteurs tiennent sur 32 bits -> on a a_p et a_q

Donc on connait les 896 MSB de p et de q.

-> Coppersmith, on trouve p et q.
