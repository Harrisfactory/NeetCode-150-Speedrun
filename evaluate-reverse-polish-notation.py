class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])
        
        token_stack = []

        operator_set = {"+","-","*","/"}

        for token in tokens:
            if token in operator_set:
                operand_one = int(token_stack.pop())
                operand_two = int(token_stack.pop())
                if token == "+":
                    token_stack.append(operand_one + operand_two)
                elif token == "-":
                    token_stack.append(operand_two - operand_one)
                elif token == "*":
                    token_stack.append(operand_one * operand_two)
                else:
                    token_stack.append(int(operand_two / operand_one))
            else:
                token_stack.append(token)
        
        return token_stack[0]