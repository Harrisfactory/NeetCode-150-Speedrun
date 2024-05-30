class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {'(':')', '{':'}', '[':']'}

        open_brackets = []

        for bracket in s:
            if bracket in brackets:#open bracket found, add to stack
                open_brackets.append(bracket)
            elif len(open_brackets) > 0:#closed bracket found and there are open brackets on stack
                if brackets[open_brackets.pop()] != bracket:
                    return False
            else:#closed bracket found and no open brackets on stack
                return False
        
        if len(open_brackets) > 0:
            return False
        return True