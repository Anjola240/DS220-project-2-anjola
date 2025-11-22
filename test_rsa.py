"""
Test suite for RSA implementation
"""

import rsa


def test_gcd():
    """Test the GCD function."""
    assert rsa.gcd(48, 18) == 6
    assert rsa.gcd(17, 13) == 1
    assert rsa.gcd(100, 50) == 50
    print("✓ GCD tests passed")


def test_mod_inverse():
    """Test modular inverse calculation."""
    # e * d ≡ 1 (mod phi)
    e = 7
    phi = 40
    d = rsa.mod_inverse(e, phi)
    assert (e * d) % phi == 1
    print("✓ Modular inverse tests passed")


def test_is_prime():
    """Test primality checking."""
    # Known primes
    assert rsa.is_prime(2)
    assert rsa.is_prime(3)
    assert rsa.is_prime(17)
    assert rsa.is_prime(97)
    
    # Known composites
    assert not rsa.is_prime(1)
    assert not rsa.is_prime(4)
    assert not rsa.is_prime(15)
    assert not rsa.is_prime(100)
    print("✓ Primality tests passed")


def test_generate_prime():
    """Test prime number generation."""
    prime = rsa.generate_prime(bits=64)
    assert rsa.is_prime(prime)
    assert prime.bit_length() >= 63  # Should be close to 64 bits
    print("✓ Prime generation tests passed")


def test_keypair_generation():
    """Test RSA key pair generation."""
    public, private = rsa.generate_keypair(bits=128)
    e, n = public
    d, n2 = private
    
    # n should be the same in both keys
    assert n == n2
    
    # e and d should be multiplicative inverses mod phi
    # We can't directly test phi, but we can test encryption/decryption
    print("✓ Key pair generation tests passed")


def test_encryption_decryption_integer():
    """Test RSA encryption and decryption with integers."""
    public, private = rsa.generate_keypair(bits=256)
    
    # Test with a small integer
    message = 42
    encrypted = rsa.encrypt(public, message)
    decrypted = rsa.decrypt(private, encrypted)
    
    assert decrypted == message
    print("✓ Integer encryption/decryption tests passed")


def test_encryption_decryption_string():
    """Test RSA encryption and decryption with strings."""
    public, private = rsa.generate_keypair(bits=256)
    
    # Test with a string
    message = "Hello, RSA!"
    encrypted = rsa.encrypt(public, message)
    decrypted = rsa.decrypt(private, encrypted)
    
    assert decrypted == message
    print("✓ String encryption/decryption tests passed")


def test_different_messages():
    """Test encryption of different messages."""
    public, private = rsa.generate_keypair(bits=256)
    
    messages = ["A", "Test", "RSA is cool!", "123", "!@#$%"]
    
    for msg in messages:
        encrypted = rsa.encrypt(public, msg)
        decrypted = rsa.decrypt(private, encrypted)
        assert decrypted == msg
    
    print("✓ Multiple message tests passed")


def test_large_message():
    """Test with a longer message."""
    public, private = rsa.generate_keypair(bits=512)
    
    message = "The quick brown fox jumps over the lazy dog. " * 3
    encrypted = rsa.encrypt(public, message)
    decrypted = rsa.decrypt(private, encrypted)
    
    assert decrypted == message
    print("✓ Large message tests passed")


def run_all_tests():
    """Run all test functions."""
    print("Running RSA tests...\n")
    
    test_gcd()
    test_mod_inverse()
    test_is_prime()
    test_generate_prime()
    test_keypair_generation()
    test_encryption_decryption_integer()
    test_encryption_decryption_string()
    test_different_messages()
    test_large_message()
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
