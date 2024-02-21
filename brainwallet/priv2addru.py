'''Private key to uncompress bitcoin address
'''

import ecdsa
import hashlib
import base58

def private_key_to_public_address(private_key):
    # Step 1: Generate Public Key
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = vk.to_string()
    
    # Step 2: add 0x04 for uncompress address
    public_key = b'\x04' + public_key

    # Step 3: Convert Public Key to Public Address
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

    network_byte = b'\x00'  # Bitcoin network byte
    extended_ripemd160 = network_byte + ripemd160_hash

    # Step 4: add checksum
    checksum = hashlib.sha256(hashlib.sha256(extended_ripemd160).digest()).digest()[:4]
    address_with_checksum = extended_ripemd160 + checksum

    # Step 5: Base58Check encoding
    public_address = base58.b58encode(address_with_checksum).decode('utf-8')
    
    return public_address

# Example Usage:
private_key = b'\xe3\xb0\xc4\x42\x98\xfc\x1c\x14\x9a\xfb\xf4\xc8\x99\x6f\xb9\x24\x27\xae\x41\xe4\x64\x9b\x93\x4c\xa4\x95\x99\x1b\x78\x52\xb8\x55'
public_address = private_key_to_public_address(private_key)
print("Public Address:", public_address)
