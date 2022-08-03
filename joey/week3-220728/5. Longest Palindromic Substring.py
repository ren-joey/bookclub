class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromicMatch(s1: str, s2: str, centre = '') -> str:
            idx = 0
            try:
                while(s1[idx] == s2[idx]):
                    idx += 1
            except:
                return s1[:idx][::-1] + centre + s2[:idx]
            finally:
                return s1[:idx][::-1] + centre + s2[:idx]

        longest_palindrome = ''
        for i in range(0, len(s)):
            p1 = palindromicMatch(s[:i][::-1], s[i:])
            p2 = palindromicMatch(s[:i][::-1], s[i+1:], s[i])
            palindrome = p1 if len(p1) > len(p2) else p2
            longest_palindrome = palindrome if len(palindrome) > len(longest_palindrome) else longest_palindrome

        return longest_palindrome
