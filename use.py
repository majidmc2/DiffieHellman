from DiffieHellman import DiffieHellman

"""
Run an example Diffie-Hellman exchange
"""

a = DiffieHellman()
b = DiffieHellman()

share_key_a = a.gen_key(b.public_key)
share_key_b = b.gen_key(a.public_key)

print(share_key_a.hexdigest())
print(share_key_a.digest())

if share_key_a.digest() == share_key_b.digest():
    print("YES")
