import math
import binascii

c=0x559C8077EE6C7990AF727955B744425D3CC2D4D7D0E46F015C8958B34783L
p=0x9451A6D9C114898235148F1BC7AA32901DCAE445BC3C08BA6325968F92DBL
b=0xCDB5E946CB9913616FA257418590EBCACB76FD4840FA90DE0FA78F095873L

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
	
a = c*modinv(b,p)
aa= hex(a%p)
aa = aa[2:-1]
print binascii.unhexlify(aa) 

#HV17-zQBz-AwDg-1FEL-rUE9-GKgq
