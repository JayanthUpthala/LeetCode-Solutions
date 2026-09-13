class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if(token == '+' or token == '-' or token == '*' or token == '/'):
                # print(st)
                var1 = st.pop()
                var2 = st.pop()
                match token:
                    case '+':
                        res = var1 + var2
                        st.append(res)
                    case '-':
                        res = var2 - var1
                        st.append(res)
                    case '*':
                        res = var1 * var2
                        st.append(res)
                    case '/':
                        res = (var2/var1)
                        if(res <0): res = math.ceil(res)
                        else: res = math.floor(res)
                        st.append(res)

            elif(token != '+' or token != '-' or token != '*' or token != '/'):
                st.append(int(token))
        return st.pop()