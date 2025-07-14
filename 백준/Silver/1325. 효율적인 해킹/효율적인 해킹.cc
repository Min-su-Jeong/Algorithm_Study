#include <bits/stdc++.h>
using namespace std;

const int MAX = 10001;
int N, M, a, b, mx, dp[MAX];
bool visited[MAX];
vector<int> ret, adj[MAX];

int go(int here) {
    int cnt = 1;
    visited[here] = 1;

    for (int there: adj[here]) {
        if (visited[there]) continue;
        cnt += go(there);
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i=0; i<M; i++) {
        cin >> a >> b;
        adj[b].push_back(a);
    }

    for (int i=1; i<=N; i++) {
        memset(visited, 0, sizeof(visited));
        dp[i] = go(i);
        mx = max(mx, dp[i]);
    }

    for (int i=1; i<=N; i++) {
        if (mx == dp[i]) cout << i << ' ';
    }
    return 0;
}