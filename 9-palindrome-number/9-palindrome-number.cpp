class Solution {
public:
    bool isPalindrome(int x) {
        string palindromeString = to_string(x);
        int length = palindromeString.size() - 1;
        for (int i = 0; i < palindromeString.size(); ++i) {
           if (palindromeString.at(i) != palindromeString.at(length - i)) return false; 
        }
        return true;
    }
};