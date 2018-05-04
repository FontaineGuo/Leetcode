/*
## 020 Valid Parentheses
## Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
## determine if the input</br> string is valid.
## The brackets must close in the correct order, "()" and "()[]{}" are all valid 
## but "(]" and "([)]" are not.
*/

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        char c;
        for(int i = 0; i < s.size(); i++)
        {
            if(s[i] == '(' || s[i] == '{' ||
               s[i] == '[')
                st.push(s[i]);
            else
            {
                if(st.empty()) //前面的已经匹配完毕，则若栈为空，必定无法匹配
                    return false;
                else
                {
                    c = st.top();
                    st.pop();
                    if((c != '(' && s[i] == ')') ||
                       (c != '[' && s[i] == ']') ||
                       (c != '{' && s[i] == '}'))
                        return false;                        
                }
            }
                
        }
        return st.empty();
        
    }
};