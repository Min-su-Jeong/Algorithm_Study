#include <bits/stdc++.h>
using namespace std;

int N;
string init_s, s, pre, suf;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    cin >> init_s;
    int pos = init_s.find('*');
    pre = init_s.substr(0, pos);
    suf = init_s.substr(pos+1);

    for (int i=0; i<N; i++) {
        cin >> s;
        
        // 반례
        if (pre.size() + suf.size() > s.size()) {
            cout << "NE\n";
        } else {
            if (pre == s.substr(0, pre.size()) && suf == s.substr(s.size()-suf.size())) cout << "DA\n";
            else cout << "NE\n";
        }
    }
    return 0;
}