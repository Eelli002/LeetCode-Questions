class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = Counter(magazine)
        for char in ransomNote:
            if char in mag_dict:
                if mag_dict[char] <= 0: return False
                else: mag_dict[char] -= 1
            else: return False
        return True