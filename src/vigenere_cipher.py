def generate_vigenere_table():
    """Generate the Vigenère table (26x26 matrix of shifted alphabets)"""
    table = []
    for i in range(26):
        row = []
        for j in range(26):
            # Calculate shifted letter
            letter = chr(((i + j) % 26) + ord('A'))
            row.append(letter)
        table.append(row)
    return table


def prepare_text(text):
    """Remove non-alphabetic characters and convert to uppercase"""
    return ''.join(char.upper() for char in text if char.isalpha())


def prepare_key(key, message_length):
    """Repeat the key to match the message length"""
    key = prepare_text(key)
    return (key * (message_length // len(key) + 1))[:message_length]


def encrypt(plaintext, key):
    """Encrypt the plaintext using Vigenère cipher"""
    table = generate_vigenere_table()
    plaintext = prepare_text(plaintext)
    key = prepare_key(key, len(plaintext))
    ciphertext = ''
    
    for p, k in zip(plaintext, key):
        # Find row and column indices in the Vigenère table
        row = ord(k) - ord('A')
        col = ord(p) - ord('A')
        # Get encrypted character from the table
        ciphertext += table[row][col]
    
    return ciphertext


def decrypt(ciphertext, key):
    """Decrypt the ciphertext using Vigenère cipher"""
    table = generate_vigenere_table()
    ciphertext = prepare_text(ciphertext)
    key = prepare_key(key, len(ciphertext))
    plaintext = ''
    
    for c, k in zip(ciphertext, key):
        # Find the row in the table corresponding to the key character
        row = ord(k) - ord('A')
        # Find the position of the ciphertext character in that row
        col = table[row].index(c)
        # Convert column index back to plaintext character
        plaintext += chr(col + ord('A'))
    
    return plaintext


# Example usage
if __name__ == "__main__":
    # Test the implementation
    message = "Hello World!"
    key = "SECRET"
    
    print(f"Original message: {message}")
    print(f"Key: {key}")
    
    encrypted = encrypt(message, key)
    print(f"Encrypted text: {encrypted}")
    
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted text: {decrypted}")