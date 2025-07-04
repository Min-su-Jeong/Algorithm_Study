#include <bits/stdc++.h>
using namespace std;

int N, s, e, ret=1;
vector<pair<int, int>> v;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> s >> e;
        v.push_back({e, s});
    }
    sort(v.begin(), v.end());

    s = v[0].second;
    e = v[0].first;
    for (int i=1; i<N; i++) {
        if (v[i].second < e) continue;
        s = v[i].second;
        e = v[i].first;
        ret++;
    }
    cout << ret << '\n';

    return 0;
}