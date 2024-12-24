import unittest
from src.vigenere_cipher import encrypt, decrypt, prepare_text, prepare_key, generate_vigenere_table


class TestVigenereCipher(unittest.TestCase):
    def setUp(self):
        """Set up some test cases to be used across multiple tests"""
        self.test_cases = [
            {
                'plaintext': 'HELLO',
                'key': 'KEY',
                'expected_cipher': 'RIJVS'
            },
            {
                'plaintext': 'ATTACKATDAWN',
                'key': 'LEMON',
                'expected_cipher': 'LXFOPVEFRNHR'
            },
            {
                'plaintext': 'PYTHONPROGRAMMING',
                'key': 'CODE',
                'expected_cipher': 'RMLVSDEPVKFOCAKR'
            }
        ]

    def test_vigenere_table_generation(self):
        """Test if the Vigenère table is generated correctly"""
        table = generate_vigenere_table()
        
        # Test table dimensions
        self.assertEqual(len(table), 26, "Table should have 26 rows")
        self.assertEqual(len(table[0]), 26, "Table should have 26 columns")
        
        # Test first row (should be regular alphabet)
        expected_first_row = [chr(i + ord('A')) for i in range(26)]
        self.assertEqual(table[0], expected_first_row, "First row should be regular alphabet")
        
        # Test that each row is shifted by one
        for i in range(1, 26):
            for j in range(26):
                expected = chr(((j + i) % 26) + ord('A'))
                self.assertEqual(table[i][j], expected, f"Incorrect shift at position [{i}][{j}]")

    def test_text_preparation(self):
        """Test text preparation function"""
        test_cases = [
            ("Hello, World!", "HELLOWORLD"),
            ("ABC 123", "ABC"),
            ("Test@#$Case", "TESTCASE"),
            ("Mixed CASE text", "MIXEDCASETEXT"),
            ("", "")
        ]
        
        for input_text, expected in test_cases:
            with self.subTest(input_text=input_text):
                self.assertEqual(prepare_text(input_text), expected)

    def test_key_preparation(self):
        """Test key preparation function"""
        test_cases = [
            ("KEY", "HELLO", "KEYKE"),
            ("LEMON", "ATTACKATDAWN", "LEMONLEMONLE"),
            ("A", "TEST", "AAAA"),
            ("LONG", "HI", "LO")
        ]
        
        for key, message, expected in test_cases:
            with self.subTest(key=key, message=message):
                self.assertEqual(prepare_key(key, len(prepare_text(message))), expected)

    def test_encryption(self):
        """Test encryption with various inputs"""
        for case in self.test_cases:
            with self.subTest(plaintext=case['plaintext']):
                result = encrypt(case['plaintext'], case['key'])
                self.assertEqual(result, case['expected_cipher'])

    def test_decryption(self):
        """Test decryption with various inputs"""
        for case in self.test_cases:
            with self.subTest(ciphertext=case['expected_cipher']):
                result = decrypt(case['expected_cipher'], case['key'])
                self.assertEqual(result, case['plaintext'])

    def test_encryption_decryption_cycle(self):
        """Test that encryption followed by decryption returns original text"""
        test_texts = [
            "THISISASECRETMESSAGE",
            "PYTHONPROGRAMMING",
            "UNITTESTINGISIMPORTANT"
        ]
        test_keys = ["SECRET", "CODE", "TEST"]
        
        for text, key in zip(test_texts, test_keys):
            with self.subTest(text=text, key=key):
                encrypted = encrypt(text, key)
                decrypted = decrypt(encrypted, key)
                self.assertEqual(decrypted, text)

    def test_empty_input(self):
        """Test handling of empty input"""
        self.assertEqual(encrypt("", "KEY"), "")
        self.assertEqual(decrypt("", "KEY"), "")

    def test_special_characters(self):
        """Test handling of special characters and spaces"""
        plaintext = "Hello, World! 123"
        key = "KEY"
        expected_cipher = encrypt("HELLOWORLD", "KEY")
        self.assertEqual(encrypt(plaintext, key), expected_cipher)

    def test_case_insensitivity(self):
        """Test that the cipher is case-insensitive"""
        plaintext = "Hello"
        key = "Key"
        upper_result = encrypt(plaintext.upper(), key.upper())
        lower_result = encrypt(plaintext.lower(), key.lower())
        mixed_result = encrypt(plaintext, key)
        
        self.assertEqual(upper_result, lower_result)
        self.assertEqual(upper_result, mixed_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
