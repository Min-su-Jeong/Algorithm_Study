#include <bits/stdc++.h>
using namespace std;

const int MAX = 32004;
int N, M, a, b, indegree[MAX];
vector<int> adj[MAX];
priority_queue<int, vector<int>, greater<int>> pq;

int main() {
    scanf("%d %d", &N, &M);
    while (M--) {
        scanf("%d %d", &a, &b);
        adj[a].push_back(b);
        indegree[b]++;
    }

    for (int i=1; i<=N; i++) {
        if (indegree[i] == 0) pq.push(i);
    }

    while (pq.size()) {
        int cur = pq.top();
        pq.pop();
        printf("%d ", cur);

        for (int i=0; i<adj[cur].size(); i++) {
            int next = adj[cur][i];
            indegree[next]--;
            if (indegree[next] == 0) pq.push(next);
        }
    }
    return 0;
}