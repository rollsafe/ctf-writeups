from Crypto.Util.number import inverse

p = 42821
q = 54727
e = 23531
tot = (p - 1) * (q - 1)
d = inverse(e, tot)

data = [
0x1A400138, 0x279AB867, 0x177D2969, 0x0E6E46F5, 0x512621F8, 0x2E96CE73,
0x0484B496, 0x73414F6E, 0x0484B496, 0x01C274E9, 0x0484B496, 0x637DC762,
0x15147A4A, 0x1FE9895E, 0x1FE9895E, 0x862B01EB, 0x775A06CD, 0x0E6E46F5,
0x0E6E46F5, 0x3E6A2466, 0x0300AB6D, 0x5A67CC12, 0x34167E01, 0x862B01EB,
0x0300AB6D, 0x0484B496, 0x862B01EB, 0x0300AB6D, 0x11EFDA4D, 0x512621F8,
0x0E6E46F5, 0x177D2969, 0x2E96CE73, 0x15147A4A, 0x5A67CC12, 0x2E96CE73,
0x7880144D, 0x5A69ED6B,
]

print(bytes([pow(m, d, p*q) for m in data]))
