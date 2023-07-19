#!/usr/bin/env python3
validate_password = __import__('6-password').validate_password

# Test cases
print(validate_password("Abcd1234"))  # True
print(validate_password("abcD1234"))  # True
print(validate_password("abcdefgh"))  # False (no uppercase letter)
print(validate_password("ABCDEFGH"))  # False (no lowercase letter)
print(validate_password("12345678"))  # False (no uppercase letter or lowercase letter)
print(validate_password("Abcd 1234")) # False (contains space)
