class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        word_list = list(word)

        if len(word) <= 1 :
            return True

        is_first_upper = word[0].isupper()
        is_second_upper = word[1].isupper()


        if is_first_upper and is_second_upper:

            for char in word:
                if not char.isupper():
                    return False
            
            return True
        
        elif is_first_upper and not is_second_upper:

            for i in range(2, len(word_list)):
                if word[i].isupper():
                    return False
            
            return True
        
        elif not is_first_upper and not is_second_upper:

            for char in word:
                if char.isupper():
                    return False
            
            return True
