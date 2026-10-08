class Solution {
public:
    string removeOuterParentheses(string s) {
        string res;
        int level = 0;
        for (char c: s) {
            if (c == ')') level --;
            if (level > 0) res += c;
            if (c == '(') level++;
        }
        return res;
    }
};