class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse =[]
        for str in s:
            if str.isalnum():
                reverse.append(str.lower())
        reverse1="".join(reverse)
        return reverse1 == reverse1[::-1]
        