# This code help you to compare hashes and crack password using Dictionary
import hashlib

def encrypt_string(plain_string):
    sha_signature = hashlib.sha256(plain_string.encode()).hexdigest()
    return sha_signature

plainText = str(input("Enter any string:- "))

print(encrypt_string(plainText))