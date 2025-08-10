#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, K;
    cin >> N >> K;

    vector<int> dp(K+1, 0);
    for (int i=0; i<N; i++) {
        int W, V;
        cin >> W >> V;

        for (int j=K; j>=W; j--) {
            dp[j] = max(dp[j], dp[j-W] + V);
        }
    }
    cout << dp[K] << '\n';

    return 0;
}