#include <bits/stdc++.h>
using namespace std;

int N, M, a, b;
map<int, int> mp;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i=1; i<=N; i++) mp[i] = i;
    for (int i=1; i<=M; i++) {
        cin >> a >> b;
        swap(mp[a], mp[b]);
    }
    for (int i=1; i<=N; i++) cout << mp[i] << ' ';

    return 0;
}