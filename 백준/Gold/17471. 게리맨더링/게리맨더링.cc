#include <bits/stdc++.h>
using namespace std;

const int MAX = 14;
const int INF = INT_MAX;
int N, M, a[MAX], tmp, sec[MAX], visited[MAX], ret=INF;
vector<int> adj[MAX];

pair<int, int> dfs(int here, int val) {
    visited[here] = 1;
    pair<int, int> ret = {1, a[here]};
    for (int there: adj[here]) {
        if (visited[there]) continue;
        if (sec[there] != val) continue;
        pair<int, int> _tmp = dfs(there, val);
        ret.first += _tmp.first;
        ret.second += _tmp.second;
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=1; i<=N; i++) cin >> a[i];
    for (int i=1; i<=N; i++) {
        cin >> M;
        for (int j=0; j<M; j++) {
            cin >> tmp;
            adj[i].push_back(tmp);
            adj[tmp].push_back(i);
        }
    }
    for (int i=1; i < (1 << N) - 1; i++) {
        fill(sec, sec + MAX, 0);
        fill(visited, visited + MAX, 0);
        int idx1 = -1, idx2 = -1;

        for (int j=0; j<N; j++) {
            if (i & (1 << j)) {
                sec[j+1] = 1;
                idx1 = j+1;
            } else {
                idx2 = j+1;
            }
        }
        pair<int, int> sec1 = dfs(idx1, 1);
        pair<int, int> sec2 = dfs(idx2, 0);
        if (sec1.first + sec2.first == N) ret = min(ret, abs(sec1.second - sec2.second));
    }
    cout << (ret == INF ? -1 : ret) << '\n';
    
    return 0;
}