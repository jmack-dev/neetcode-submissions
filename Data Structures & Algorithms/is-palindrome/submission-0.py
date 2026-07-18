import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = string.ascii_letters + string.digits
        clean = []
        for c in s:
            if 48 <= ord(c) <= 57 or 65 <= ord(c) <= 90:
                clean.append(c)
            if 97 <= ord(c) <= 122:
                clean.append( chr(ord(c) - 32))
        return clean == list(reversed(clean))