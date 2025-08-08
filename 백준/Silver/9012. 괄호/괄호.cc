#include <bits/stdc++.h>
using namespace std;

int T;
string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> T;
    while (T--) {
        stack<char> stk;

        cin >> s;
        for (char c: s) {
            if (stk.size() && stk.top() == '(' && c == ')') stk.pop();
            else stk.push(c);
        }
        if (stk.size()) cout << "NO\n";
        else cout << "YES\n";
    }
    return 0;
}