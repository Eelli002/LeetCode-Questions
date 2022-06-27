class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = []
        curr_word = ""
        
        for i in range(len(s)):
            if s[i] != ' ':
                curr_word += s[i]
                
            elif len(curr_word) != 0:
                str_list.append(curr_word)
                curr_word = ""
                
            else: curr_word = ""
        if len(curr_word) > 0: str_list.append(curr_word)
        
        reversed_str = str_list[len(str_list)-1]
        for i in range(len(str_list)-2, -1, -1):
            reversed_str += " " + str_list[i]
            
        print(str_list)
            
        return reversed_str
        
        