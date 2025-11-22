# RSA Encryption Implementation

This directory contains a Python implementation of the RSA (Rivest-Shamir-Adleman) encryption algorithm.

## Files

- **rsa.py**: Main RSA implementation module with key generation, encryption, and decryption functions
- **test_rsa.py**: Comprehensive test suite for the RSA implementation

## Features

- RSA key pair generation (public and private keys)
- Message encryption using public key
- Message decryption using private key
- Support for both string and integer encryption
- Miller-Rabin primality testing for secure prime generation
- Configurable key size

## Usage

### Basic Example

```python
import rsa

# Generate key pair
public_key, private_key = rsa.generate_keypair(bits=512)

# Encrypt a message
message = "Hello, World!"
encrypted = rsa.encrypt(public_key, message)

# Decrypt the message
decrypted = rsa.decrypt(private_key, encrypted)
print(decrypted)  # Output: Hello, World!
```

### Integer Encryption

```python
import rsa

public_key, private_key = rsa.generate_keypair(bits=512)

# Encrypt a number
number = 42
encrypted_num = rsa.encrypt(public_key, number)
decrypted_num = rsa.decrypt(private_key, encrypted_num)
print(decrypted_num)  # Output: 42
```

## Running the Demo

```bash
python rsa.py
```

## Running Tests

```bash
python test_rsa.py
```

## Functions

### `generate_keypair(bits=512)`
Generates a public and private key pair.
- **Parameters**: `bits` - Size of each prime number in bits (default: 512)
- **Returns**: `((e, n), (d, n))` - Public key (e, n) and private key (d, n)

### `encrypt(public_key, plaintext)`
Encrypts a message using the public key.
- **Parameters**: 
  - `public_key` - Tuple (e, n)
  - `plaintext` - String or integer to encrypt
- **Returns**: Encrypted data (list for strings, integer for numbers)

### `decrypt(private_key, ciphertext)`
Decrypts a message using the private key.
- **Parameters**:
  - `private_key` - Tuple (d, n)
  - `ciphertext` - Encrypted data
- **Returns**: Decrypted string or integer

## Security Notes

- This is an educational implementation
- For production use, consider established libraries like `cryptography` or `pycryptodome`
- Default key size is 512 bits; for real-world applications, use at least 2048 bits
- The implementation includes Miller-Rabin primality testing for secure prime generation

## Algorithm Overview

RSA is based on the mathematical difficulty of factoring large composite numbers. The algorithm works as follows:

1. **Key Generation**:
   - Generate two large prime numbers (p and q)
   - Calculate n = p × q
   - Calculate φ(n) = (p-1) × (q-1)
   - Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
   - Calculate d such that d × e ≡ 1 (mod φ(n))
   - Public key: (e, n), Private key: (d, n)

2. **Encryption**: ciphertext = plaintext^e mod n

3. **Decryption**: plaintext = ciphertext^d mod n
