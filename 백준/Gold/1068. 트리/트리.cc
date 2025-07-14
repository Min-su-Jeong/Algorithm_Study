#include <bits/stdc++.h>
using namespace std;

int N, r, root, node;
vector<int> adj[54];

int go(int here) {
    if (here == r) return 0;

    int ret = 0, child = 0;
    for (int there: adj[here]) {
        if (there == r) continue;
        ret += go(there);
        child++;
    }
    if (child == 0) return 1;

    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> node;
        if (node == -1) root = i;
        else adj[node].push_back(i);
    }
    cin >> r;

    cout << go(root) << '\n';
    return 0;
}