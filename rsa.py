"""
RSA Encryption/Decryption Implementation

This module provides basic RSA encryption and decryption functionality.
RSA (Rivest-Shamir-Adleman) is a public-key cryptosystem.
"""

import random
import math


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    """
    Calculate the modular multiplicative inverse of e modulo phi.
    Uses the Extended Euclidean Algorithm.
    """
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    _, x, _ = extended_gcd(e, phi)
    return (x % phi + phi) % phi


def is_prime(n, k=5):
    """
    Miller-Rabin primality test.
    
    Args:
        n: Number to test for primality
        k: Number of rounds (higher k means more accurate)
    
    Returns:
        True if n is probably prime, False if n is composite
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def generate_prime(bits=512):
    """
    Generate a random prime number with the specified number of bits.
    
    Args:
        bits: Number of bits for the prime number
    
    Returns:
        A prime number
    """
    while True:
        # Generate a random odd number
        num = random.getrandbits(bits)
        num |= (1 << (bits - 1)) | 1  # Set MSB and LSB to 1 for clarity
        
        if is_prime(num):
            return num


def generate_keypair(bits=512):
    """
    Generate RSA public and private key pair.
    
    Args:
        bits: Size of the prime numbers in bits (key size will be 2*bits)
    
    Returns:
        Tuple of ((e, n), (d, n)) where:
        - (e, n) is the public key
        - (d, n) is the private key
    """
    # Generate two distinct prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    
    # Calculate n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e from standard secure values
    # Common choices: 3, 17, 257, 65537 (Fermat primes)
    candidates = [65537, 257, 17, 3]
    e = None
    for candidate in candidates:
        if gcd(candidate, phi) == 1:
            e = candidate
            break
    
    # Fallback if none of the standard values work
    if e is None:
        e = 2
        while gcd(e, phi) != 1:
            e += 1
    
    # Calculate d (modular multiplicative inverse of e)
    d = mod_inverse(e, phi)
    
    # Public key: (e, n), Private key: (d, n)
    return ((e, n), (d, n))


def encrypt(public_key, plaintext):
    """
    Encrypt a message using RSA public key.
    
    Args:
        public_key: Tuple (e, n) representing the public key
        plaintext: String or integer to encrypt
    
    Returns:
        Encrypted integer or list of encrypted integers
    """
    e, n = public_key
    
    # Handle string input
    if isinstance(plaintext, str):
        # Convert each character to encrypted integer
        return [pow(ord(char), e, n) for char in plaintext]
    else:
        # Handle integer input
        return pow(plaintext, e, n)


def decrypt(private_key, ciphertext):
    """
    Decrypt a message using RSA private key.
    
    Args:
        private_key: Tuple (d, n) representing the private key
        ciphertext: Encrypted integer or list of encrypted integers
    
    Returns:
        Decrypted string or integer
    """
    d, n = private_key
    
    # Handle list input (encrypted string)
    if isinstance(ciphertext, list):
        # Decrypt each integer and convert back to character
        return ''.join([chr(pow(char, d, n)) for char in ciphertext])
    else:
        # Handle integer input
        return pow(ciphertext, d, n)


if __name__ == "__main__":
    # Demo usage
    print("Generating RSA key pair...")
    public, private = generate_keypair(bits=256)
    print(f"Public key: {public}")
    print(f"Private key: {private}")
    
    # Test with string
    message = "Hello, RSA!"
    print(f"\nOriginal message: {message}")
    
    encrypted = encrypt(public, message)
    print(f"Encrypted: {encrypted[:3]}...")  # Show first 3 encrypted chars
    
    decrypted = decrypt(private, encrypted)
    print(f"Decrypted: {decrypted}")
    
    # Test with integer
    num = 42
    print(f"\nOriginal number: {num}")
    encrypted_num = encrypt(public, num)
    print(f"Encrypted: {encrypted_num}")
    decrypted_num = decrypt(private, encrypted_num)
    print(f"Decrypted: {decrypted_num}")
