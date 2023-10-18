class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for char in s:
            if char != ']':
                stack.append(char)
            # kick off decode after meeting ]
            else:
                temp_str=""
                # get letter in []
                while stack[-1] != '[':
                    stack_top=stack.pop()
                    temp_str = stack_top + temp_str
                # pop up [
                stack.pop()

                # get digital string
                digital=""
                while stack and stack[-1].isdigit():
                    stack_top=stack.pop()
                    digital = stack_top + digital
                # add decoded string into stack
                stack.append(int(digital)*temp_str)
        #combine all letters in stack(list) 
        return "".join(stack)

                

