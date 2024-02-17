'''Brainwallet in python 3
priv = sha256(password)

Usage: python brain2priv.py "satoshi"
da2876b3eb31edb4436fa4650673fc6f01f90de2f1793c4ec332b2387b09726f
'''

import sys
import hashlib

def brain2priv():
    brain = sys.argv[1]
    priv = hashlib.sha256(brain.encode('utf-8')).hexdigest()
    print(priv)
    
if __name__ == '__main__':
    brain2priv()
