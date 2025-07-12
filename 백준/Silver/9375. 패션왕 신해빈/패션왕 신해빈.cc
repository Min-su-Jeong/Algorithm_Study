#include <bits/stdc++.h>
using namespace std;

int t, n;
string a, b;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> t;
    while (t--) {
        int ret = 1;
        map<string, int> mp;

        cin >> n;
        for (int i=0; i<n; i++) {
            cin >> a >> b;
            mp[b]++;
        }
        for (auto it: mp) ret *= (it.second+1);
        cout << ret-1 << '\n';
    }
    return 0;
}