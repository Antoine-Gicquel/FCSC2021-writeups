from fastecdsa.curve import Curve
from fastecdsa.point import Point
from Crypto.Util.number import getPrime
from Crypto.Random.random import randrange

BITS = 80

while True:
	p = getPrime(BITS)
	if p % 4 == 3:
		break

a, b = randrange(1, p), randrange(1, p)
C = Curve("FCSC", p, a, b, 0, 0, 0)

while True:
	xP = randrange(1, p)
	yP = (xP ** 3 + a * xP + b) % p
	if pow(yP, (p - 1) // 2, p) == 1:
		break

yP = pow(yP, (p + 1) // 4, p)
assert (xP ** 3 + a * xP + b - yP ** 2) % p == 0

P = Point(xP, yP, C)
Q = 2 * P

print("Can you find my secret curve equation: y^2 = x^3 + a*x + b (mod p)?")
print("I will give you two points:")
print(f"P = ({P.x}, {P.y})")
print(f"Q = ({Q.x}, {Q.y})")

try:
	a = int(input(">>> a = "))
	b = int(input(">>> b = "))
	p = int(input(">>> p = "))

	C = Curve("Check", p, a, b, 0, 0, 0)
	check  = True
	check &= p.bit_length() >= BITS
	check &= (P.x ** 3 + a * P.x + b - P.y ** 2) % p == 0
	check &= (Q.x ** 3 + a * Q.x + b - Q.y ** 2) % p == 0
	check &= (2 * Point(P.x, P.y, C) == Point(Q.x, Q.y, C))
	if check:
		print("Congratulations!! Here is your flag:")
		print(open("flag.txt", "r").read())
	else:
		print("That's not it!")
except:
	print("That's not it!")
