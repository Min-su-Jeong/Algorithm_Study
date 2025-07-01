#include <bits/stdc++.h>
using namespace std;

int T;
string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> T;
    while (T--) {
        cin >> s;
        cout << s.front() << s.back() << '\n';
    }
    return 0;
}