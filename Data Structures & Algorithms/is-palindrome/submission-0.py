class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse= []
        for ch in s:
            if ch.isalnum():
                reverse.append(ch.lower())
        if reverse == reverse[::-1]:
            return True
        else:
            return False
        