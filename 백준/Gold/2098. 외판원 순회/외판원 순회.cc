#include <bits/stdc++.h>
using namespace std;

const int MAX = 16;
const int INF = 987654321;
int N, w[MAX][MAX], dp[MAX][1 << MAX];

int tsp(int here, int visited) {
    if (visited == (1 << N) - 1) {
        return w[here][0] ? w[here][0] : INF;
    }
    int &ret = dp[here][visited];
    if (ret != -1) return ret;

    ret = INF;
    for (int i=0; i<N; i++) {
        if (visited & (1 << i)) continue;
        if (w[here][i] == 0) continue;
        ret = min(ret, tsp(i, visited | (1 << i)) + w[here][i]);
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> w[i][j];
        }
    }
    
    memset(dp, -1, sizeof(dp));
    cout << tsp(0, 1) << '\n';

    return 0;
}