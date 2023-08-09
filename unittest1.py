import re
import unittest

def validate_email(email):
    valid_providers = ["yahoo.com", "gmail.com", "outlook.com"]

    if not re.match(r"[^@ ]+@[^@ ]+\.[^@ ]+", email):
        return False
    _, domain = email.split('@')
    if domain not in valid_providers:
        return False
    return True

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "john.doe@gmail.com",
            "jane_smith@yahoo.com",
            "user@outlook.com",
        ]

        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email),
                                f"{email} should be valid")

    def test_invalid_emails(self):
        invalid_emails = [
            "invalidemail.com",
            "john.doe@gmail",
            "user@yopmail.com",
        ]

        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email),
                                 f"{email} should be invalid")
