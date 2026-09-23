class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alphanums = "".join(filter(str.isalnum, s.lower()))
        return only_alphanums == only_alphanums[::-1]