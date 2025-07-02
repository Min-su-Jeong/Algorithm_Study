#include <bits/stdc++.h>
using namespace std;

string s, bomb, ret;
stack<char> stk;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> s >> bomb;
    for (char c: s) {
        stk.push(c);
        if (stk.size() >= bomb.size() && stk.top() == bomb.back()) {
            string ss = "";
            for (char b: bomb) {
                ss += stk.top();
                stk.pop();
            }
            reverse(ss.begin(), ss.end());
            if (ss != bomb) {
                for (char b: ss) stk.push(b);
            }
        }
    }
    if (!stk.size()) cout << "FRULA\n";
    else {
        while (stk.size()) {
            ret += stk.top(); 
            stk.pop();
        }
        reverse(ret.begin(), ret.end());
        cout << ret << '\n';
    } 
    return 0;
}