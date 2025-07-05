#include <bits/stdc++.h>
using namespace std;

int N, L, r, cnt, ret;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> L;
    vector<pair<int, int>> v(N);
    for (int i=0; i<N; i++) cin >> v[i].first >> v[i].second;
    sort(v.begin(), v.end());

    for (int i=0; i<N; i++) {
        if (v[i].second <= r) continue;
        if (r < v[i].first) {
            int len = v[i].second - v[i].first;
            cnt = len / L + (len % L ? 1 : 0);
            r = v[i].first + cnt * L;
        } else {
            int len = v[i].second - r;
            cnt = len / L + (len % L ? 1 : 0);
            r = r + cnt * L;
        }
        ret += cnt;
    }
    cout << ret << '\n';

    return 0;
}