On entend les bits de dp et dq, en commençant par les bits de poids fort. Quand y'a 3 pics c'est un 1, quand y'en a 2 c'est un 0. Parsing avec Python, puis factorisation de N à partir de dp et dq :
```Python
c = powmod(2, e, n)
mp = pow(c, dp, n)
p = math.gcd(m-mp, n)
```

Une fois N factorisé, trivial.
