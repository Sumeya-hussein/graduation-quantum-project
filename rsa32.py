import random
from math import gcd

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def generate_prime(bits):
    while True:
        prime_candidate = random.getrandbits(bits)
        prime_candidate |= (1 << bits - 1) | 1
        if is_prime(prime_candidate):
            return prime_candidate

def multiplicative_inverse(e, phi):
    x, y, u, v = 0, 1, 1, 0
    a, b = e, phi
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u*q, y - v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x % phi

def generate_keys():
    p = generate_prime(16)
    q = generate_prime(16)
    while q == p:
        q = generate_prime(16)
    n = p * q
    phi = (p - 1)*(q - 1)
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def pad_message(message, block_size=4):
    padded = message.encode('utf-8')
    while len(padded) % block_size != 0:
        padded += b'\x00'
    return padded

def encrypt(message, pub_key):
    e, n = pub_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher

def decrypt(ciphertext, priv_key):
    d, n = priv_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain).rstrip('\x00')

if __name__ == "__main__":
    public_key, private_key = generate_keys()
    message = "HELLO RSA"
    print(f"Public key: {public_key}")
    print(f"Private key: {private_key}")

    cipher_text = encrypt(message, public_key)
    print(f"Encrypted message: {cipher_text}")

    decrypted_message = decrypt(cipher_text, private_key)
    print(f"Decrypted message: {decrypted_message}")
