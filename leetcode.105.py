class Solution {
public:
    int evalRPN(vector<string>& tokens) {

        stack<int> st;
        int a, b;

        for (string c : tokens) {
            if (c == "+") {
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                st.push(a + b);

            } else if (c == "-") {
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                st.push(a - b);

            } else if (c == "*") {
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                st.push(a * b);
            } else if (c == "/") {
                b = st.top();
                st.pop();
                a = st.top();
                st.pop();
                st.push(a / b);
            } else {
                st.push(stoi(c));
            }
        }

        return st.top();
    }
};
