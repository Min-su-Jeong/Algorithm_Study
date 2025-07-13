#include <bits/stdc++.h>
using namespace std;

int a[27], flag;
string s, ret;
char mid;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> s;
    for (char c: s) a[c-'A']++;

    for (int i=26; i>=0; i--) {
        if (a[i]) {
            if (a[i] & 1) {
                mid = char(i + 'A');
                a[i]--;
                flag++;
            }

            if (flag == 2) break;

            for (int j=0; j<a[i]; j+=2) {
                ret = char(i+'A') + ret + char(i+'A');
            }
        }
    }
    if (mid) ret.insert(ret.begin() + ret.size()/2, mid);

    if (flag == 2) cout << "I'm Sorry Hansoo";
    else cout << ret << '\n';

    return 0;
}