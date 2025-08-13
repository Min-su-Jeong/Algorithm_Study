#include <bits/stdc++.h>
using namespace std;

int N, K, dp[101][100001];
struct Cost {
    int _time, pay;
};
Cost a[101], b[101];

int go(int here, int _time) {
    if (here == N) return 0;
    int &ret = dp[here][_time];
    if (ret) return ret;
    ret = -1e6;
    if (_time - a[here]._time >= 0) ret = max(ret, go(here+1, _time-a[here]._time) + a[here].pay);
    if (_time - b[here]._time >= 0) ret = max(ret, go(here+1, _time-b[here]._time) + b[here].pay);
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> K;
    for (int i=0; i<N; i++) {
        cin >> a[i]._time >> a[i].pay >> b[i]._time >> b[i].pay;
    }
    cout << go(0, K) << '\n';
    return 0;
}