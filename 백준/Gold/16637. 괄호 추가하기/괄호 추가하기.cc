#include <bits/stdc++.h>
using namespace std;

int N, ret = INT_MIN;
string s;
vector<int> digit;
vector<char> op;

int oper(int a, int b, int c) {
    if (a == '+') return b + c;
    if (a == '-') return b - c;
    if (a == '*') return b * c;
}

void go(int idx, int psum) {
    if (idx == digit.size() - 1) {
        ret = max(ret, psum);
        return;
    }
    go(idx+1, oper(op[idx], psum, digit[idx+1]));
    if (idx+2 <= digit.size() - 1) {
        int tmp = oper(op[idx+1], digit[idx+1], digit[idx+2]);
        go(idx+2, oper(op[idx], psum, tmp));
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    cin >> s;
    for (int i=0; i<N; i++) {
        if (i % 2) op.push_back(s[i]);
        else digit.push_back(s[i] - '0'); 
    }
    go(0, digit[0]);
    cout << ret << '\n';

    return 0;
}