#include <bits/stdc++.h>
using namespace std;

const int MAX = 24;
int N, M, C, a[MAX], dp[MAX][1 << 14][MAX];

int go(int here, int steal, int capacity) {
    if (here == M) return 0;
    int &ret = dp[here][steal][capacity];
    if (ret) return ret;
    ret = max(ret, go(here+1, steal, C));
    for (int i=0; i<N; i++) {
        bool before = (1 << i) & steal;
        bool after = (capacity - a[i]) >= 0;
        if (!before && after) ret = max(ret, go(here, steal | (1 << i), capacity-a[i]) + 1);
    }
    return ret;
}   

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M >> C;
    for (int i=0; i<N; i++) cin >> a[i];

    cout << go(0, 0, C) << '\n';
    return 0;
}