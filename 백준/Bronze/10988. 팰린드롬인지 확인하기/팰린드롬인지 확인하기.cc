#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, r;
    cin >> s;
    r = s;
    reverse(r.begin(), r.end());

    cout << (r == s) ? 1 : 0 << '\n';

    return 0;
}