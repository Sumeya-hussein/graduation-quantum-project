# quantum_payload.py

from rsa32 import generate_keys, encrypt

# 1) Generate a fresh RSA-32 keypair
public_key, _ = generate_keys()
n = public_key[1]

# 2) Encrypt a sample message
message = "QUANTUM"
cipher = encrypt(message, public_key)

# 3) Export the payload dict at module scope
payload_for_quantum_attack = {
    "modulus_n": n,
    "encrypted_message": cipher
}

if __name__ == "__main__":
    print("Payload prepared for quantum attack (Shor's algorithm):")
    print(payload_for_quantum_attack)
