#include <bits/stdc++.h>
using namespace std;

string s, tmp;

int main() {
    cin >> s;
    tmp = s;
    reverse(tmp.begin(), tmp.end());

    if (s == tmp) cout << 1 << '\n';
    else cout << 0 << '\n';
    
    return 0;
}