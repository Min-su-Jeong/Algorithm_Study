#include <bits/stdc++.h>
using namespace std;

const int MAX = 10001;
int N, M, A, B, mx, dp[MAX];
bool visited[MAX];
vector<int> adj[MAX];

int dfs(int here) {
    int ret = 1;
    visited[here] = 1;
    for (int there: adj[here]) {
        if (visited[there]) continue;
        ret += dfs(there);
    }
    return ret;
}
int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i=0; i<M; i++) {
        cin >> A >> B;
        adj[B].push_back(A);
    }

    for (int i=1; i<=N; i++) {
        memset(visited, 0, sizeof(visited));
        dp[i] = dfs(i);
        mx = max(mx, dp[i]);
    }
    
    for(int i=1; i<=N; i++) {
        if (mx == dp[i]) cout << i << ' ';
    }
    return 0;
}