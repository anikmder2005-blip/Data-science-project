class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2==1:
            return False

        st = []

        for ch in list(s):
            #opening breckets
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)
            # closing brackets
            else:
                if len(st)==0:
                    return False
                top = st.pop()
                if ch==')' and top!='(':
                    return False
                elif ch=='}'and top!='{':
                    return False
                elif ch==']' and top!='[':
                    return False

        return len(st)==0