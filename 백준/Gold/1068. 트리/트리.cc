#include <bits/stdc++.h>
using namespace std;

int N, r, node, root;
vector<int> adj[51];

int dfs(int here) {
    if (here == r) return 0;
    
    int ret = 0; 
    int child = 0;
    for (int there: adj[here]) {
        if (there == r) continue;
        ret += dfs(there);
        child++;
    }
    if (child == 0) return 1;
    return ret; // 리프노드의 수
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> node;
        if (node == -1) root = i;
        else adj[node].push_back(i);
    }
    cin >> r;
    
    cout << dfs(root) << '\n';
    return 0;
}