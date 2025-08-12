#include <bits/stdc++.h>
using namespace std;

const int MAX = 1004;
int T, W, a[MAX], dp[MAX][2][34];

int go(int idx, int tree, int move) {
    if (move < 0) return -1e9;
    if (idx == T) return 0;
    int &ret = dp[idx][tree][move];
    if (~ret) return ret;
    return ret = max(go(idx+1, tree^1, move-1), go(idx+1, tree, move)) + (tree == a[idx] - 1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    memset(dp, -1, sizeof(dp));
    cin >> T >> W;
    for (int i=0; i<T; i++) cin >> a[i];

    cout << max(go(0, 1, W-1), go(0, 0, W)) << '\n';
    return 0;
}