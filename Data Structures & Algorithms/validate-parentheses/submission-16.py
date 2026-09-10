class Solution:
    def isValid(self, s: str) -> bool:
        
        opn_brak = "({["
        cls_brak = ")}]"
        temp_stack = []

        for char in s:
            o_index = None
            c_index = None
            if char in opn_brak:
                temp_stack.append(char)
            else:
                if len(temp_stack) == 0:
                    return False
                temp_var = temp_stack.pop()
                o_index = opn_brak.find(temp_var)
                c_index = cls_brak.find(char)
            if o_index != c_index:
                return False
        return not temp_stack
        
