def left_rotate(value, shift, bits=32):
    return ((value << shift) & (2**bits - 1)) | (value >> (bits - shift))

def right_rotate(value, shift, bits=32):
    return (value >> shift) | ((value << (bits - shift)) & (2**bits - 1))

def generate_subkeys(master_key):
    subkeys = [(master_key >> (32 * i)) & 0xFFFFFFFF for i in range(4)]
    return subkeys

def encrypt(plaintext, subkeys):
    ciphertext = plaintext
    for round in range(8):
        for subkey in subkeys:
            ciphertext = left_rotate(ciphertext, 10, 64) ^ subkey
    return ciphertext

def decrypt(ciphertext, subkeys):
    plaintext = ciphertext
    for round in range(8):
        for subkey in reversed(subkeys):
            plaintext = right_rotate(plaintext ^ subkey, 10, 64)
    return plaintext

master_key = 0x24566777777772456F53214444444442
plaintext = 0x7772456F53214444
subkeys = generate_subkeys(master_key)

print(f"Plaintext: {plaintext}")
ciphertext = encrypt(plaintext, subkeys)
print(f"Ciphertext: {ciphertext}")
decrypted_text = decrypt(ciphertext, subkeys)
print(f"Decrypted text: {decrypted_text}")