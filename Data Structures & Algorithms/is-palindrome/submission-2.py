class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse =[]
        for str in s:
            if str.isalnum():
                reverse.append(str.lower())
        return reverse == reverse[::-1]
        