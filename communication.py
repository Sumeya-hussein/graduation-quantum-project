from rsa32 import generate_keys, encrypt, decrypt, pad_message

def alice_sends(message, bob_public_key):
    padded_message = pad_message(message)
    cipher = encrypt(padded_message.decode(), bob_public_key)
    return cipher

def bob_receives(cipher, bob_private_key):
    decrypted_message = decrypt(cipher, bob_private_key)
    return decrypted_message

if __name__ == "__main__":
    public_key, private_key = generate_keys()
    message = "HELLO BOB!"
    print(f"Alice sends: {message}")

    cipher_payload = alice_sends(message, public_key)
    print(f"Encrypted payload: {cipher_payload}")

    received_payload = bob_receives(cipher_payload, private_key)
    print(f"Bob receives: {received_payload}")
