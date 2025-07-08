#include <bits/stdc++.h>
using namespace std;

int a, b, num, ret;
map<int, int> mp;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> a >> b;
    for (int i=0; i<a; i++) {
        cin >> num;
        mp[num]++;
    }
    for (int i=0; i<b; i++) {
        cin >> num;
        mp[num]++;
    }
    for (auto it: mp) {
        if (it.second == 1) ret++;
    }
    cout << ret << '\n';

    return 0;
}