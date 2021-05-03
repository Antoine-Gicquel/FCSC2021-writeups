Il faut [récupérer les clés publiques RSA](https://blog.silentsignal.eu/2021/02/08/abusing-jwt-public-keys-without-the-public-key/) utilisées pour signer les JWT (il y en a 3, indiquées par le champ kid des JWT).
Ils partagent tous un facteur. Du coup les 3 sont factorisés trivialement, on peut forger un jwt
