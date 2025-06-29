#include <bits/stdc++.h>
using namespace std;

const int MAX = 1004;
int T, N, M, a, b, cnt, visited[MAX];
vector<int> adj[MAX];

void dfs(int here) {
    visited[here] = 1;
    for (int there: adj[here]) {
        if (visited[there]) continue;
        dfs(there);
    }
    return;
}

int main() {
    scanf("%d", &T);
    while (T--) {
        cnt = 0;
        for (int i=0; i<MAX; i++) adj[i].clear();
        fill(visited, visited+MAX, 0);
        
        scanf("%d %d", &N, &M);
        for (int i=0; i<M; i++) {
            scanf("%d %d", &a, &b);
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        for (int i=1; i<=N; i++) {
            if (visited[i]) continue;
            dfs(i);
            cnt++;
        }

        if (M == N - 1 && cnt == 1) puts("tree");
        else puts("graph");
    }
    return 0;
}