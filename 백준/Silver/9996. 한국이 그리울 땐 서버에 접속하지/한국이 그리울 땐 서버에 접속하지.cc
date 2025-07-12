#include <bits/stdc++.h>
using namespace std;

int N;
string s, pattern;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    cin >> pattern;
    int pos = pattern.find("*");
    string pre = pattern.substr(0, pos);
    string suf = pattern.substr(pos+1);

    for (int i=0; i<N; i++) {
        cin >> s;
        if (pre.size() + suf.size() > s.size()) {
            cout << "NE\n";
        } else {
            if (pre == s.substr(0, pre.size()) && suf == s.substr(s.size()-suf.size())) cout << "DA\n";
            else cout << "NE\n";
        }
    }
    return 0;
}