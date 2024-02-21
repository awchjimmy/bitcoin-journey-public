import ecdsa
import hashlib
import base58
import binascii
import sys

def priv2addru(private_key):
    # Step 0: string to byte-array, then to a2b_hex format
    private_key = private_key.encode('utf-8')
    private_key = binascii.a2b_hex(private_key)
    
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

if __name__ == '__main__':
    private_key = sys.argv[1]
    public_address = priv2addru(private_key)
    print(public_address)
