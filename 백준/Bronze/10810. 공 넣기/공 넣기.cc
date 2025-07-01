#include <bits/stdc++.h>
using namespace std;

int N, M, a, b, c;
map<int, int> mp;

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(NULL); cin.tie(NULL);

    cin >> N >> M;
    for (int i=1; i<=M; i++) {
        cin >> a >> b >> c;
        for (int j=a; j<=b; j++) mp[j] = c;
    }
    for (int i=1; i<=N; i++) cout << mp[i] << ' ';

    return 0;
}