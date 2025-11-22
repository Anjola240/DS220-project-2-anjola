#!/usr/bin/env python3
"""
RSA Encryption/Decryption Example

This script demonstrates the usage of the RSA implementation.
"""

import rsa


def main():
    print("=" * 60)
    print("RSA Encryption/Decryption Example")
    print("=" * 60)
    
    # Generate RSA key pair
    print("\n1. Generating RSA key pair (512-bit)...")
    public_key, private_key = rsa.generate_keypair(bits=512)
    e, n = public_key
    d, _ = private_key
    
    print(f"   Public Key (e, n):")
    print(f"   e = {e}")
    print(f"   n = {n}")
    print(f"\n   Private Key (d, n):")
    print(f"   d = {d}")
    
    # Example 1: Encrypting and decrypting a string message
    print("\n" + "=" * 60)
    print("2. String Encryption Example")
    print("=" * 60)
    
    message = "Hello, RSA!"
    print(f"\n   Original message: '{message}'")
    
    encrypted_msg = rsa.encrypt(public_key, message)
    print(f"   Encrypted (first 3 chars): {encrypted_msg[:3]}")
    print(f"   Total encrypted characters: {len(encrypted_msg)}")
    
    decrypted_msg = rsa.decrypt(private_key, encrypted_msg)
    print(f"   Decrypted message: '{decrypted_msg}'")
    
    assert message == decrypted_msg, "Decryption failed!"
    print("   ✓ Encryption/Decryption successful!")
    
    # Example 2: Encrypting and decrypting a number
    print("\n" + "=" * 60)
    print("3. Integer Encryption Example")
    print("=" * 60)
    
    number = 123456789
    print(f"\n   Original number: {number}")
    
    encrypted_num = rsa.encrypt(public_key, number)
    print(f"   Encrypted: {encrypted_num}")
    
    decrypted_num = rsa.decrypt(private_key, encrypted_num)
    print(f"   Decrypted number: {decrypted_num}")
    
    assert number == decrypted_num, "Decryption failed!"
    print("   ✓ Encryption/Decryption successful!")
    
    # Example 3: Encrypting a longer message
    print("\n" + "=" * 60)
    print("4. Long Message Example")
    print("=" * 60)
    
    long_message = "The RSA algorithm is named after Ron Rivest, Adi Shamir, and Leonard Adleman."
    print(f"\n   Original message ({len(long_message)} chars):")
    print(f"   '{long_message}'")
    
    encrypted_long = rsa.encrypt(public_key, long_message)
    print(f"   Encrypted into {len(encrypted_long)} integer values")
    
    decrypted_long = rsa.decrypt(private_key, encrypted_long)
    print(f"   Decrypted message:")
    print(f"   '{decrypted_long}'")
    
    assert long_message == decrypted_long, "Decryption failed!"
    print("   ✓ Encryption/Decryption successful!")
    
    # Example 4: Demonstrating different key sizes
    print("\n" + "=" * 60)
    print("5. Different Key Size Example")
    print("=" * 60)
    
    test_message = "Testing key sizes"
    
    for bits in [256, 512, 1024]:
        print(f"\n   Testing with {bits}-bit keys...")
        pub, priv = rsa.generate_keypair(bits=bits)
        
        enc = rsa.encrypt(pub, test_message)
        dec = rsa.decrypt(priv, enc)
        
        assert test_message == dec, f"Decryption failed for {bits}-bit key!"
        print(f"   ✓ {bits}-bit key: Success")
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
