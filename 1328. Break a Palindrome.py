class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        for i in range(int(len(palindrome)/2)):
            if palindrome[i] != 'a':
                return f"{palindrome[:i]}a{palindrome[i + 1:]}"
        return f"{palindrome[:len(palindrome)-1]}b"
