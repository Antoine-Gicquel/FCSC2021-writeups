Idée de solution

On désassemble avec Ghidra, pour trouver l'adresse du premier break (avant les instructions que Ghidra n'arrive pas à disass)

On prend gbd, on break juste avant le bug ghidra. On se rend compte d'un pattern :
1. Le bout de code du début, qui calcule l'adresse de jump -> jump à cette adresse
2. une instruction suivie de quelques nop
3. On retourne au code du début, et on recommence


Le code du début, en python :

```python
def step_ancien_reste(r):
    return (0xd9 + r*0xb5) % 0x200

def reste_to_address(r):
    return (r << 4) + 0x40127d

reste = secret
while True:
  reste = step_ancien_reste(reste)
  addr = reste_to_address(reste)
  jump(addr)
```

On peut reverse la formule, et vérifier que tout élément de [0, 0x200] n'a qu'un seul antécédent par `step_ancien_reste`.

On peut donc retracer l'exécution du programme, en backtracking depuis l'adresse de l'instruction `ret`, afin d'obtenir l'odre des instructions et le secret qui permet de démarrer l'exécution du programme au bon endroit pour obtenir le flag.

On voit que les instructions appliquent un algorithme sur chaque caractère de notre entrée :  
A l'étape i :

1. Dupliquer entree[i]
2. XOR entree[i] || entree[i], XORKEY[i], reste[i]
3. OR r9, `2.`

L'input est correct si r9 = 0 à la fin de l'exécution.

Donc il suffit de calculer XORKEY[i] ^ reste[i] pour obtenir le caractère i du flag.
