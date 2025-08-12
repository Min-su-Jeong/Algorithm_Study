#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX = 104;
ll N, a[MAX], dp[MAX][21];

ll go(int idx, int sum) {
    if (sum < 0 || sum > 20) return 0;
    ll &ret = dp[idx][sum];
    if (ret) return ret;
    if (idx == N-2) {
        if (sum == a[N-1]) return 1;
        else return 0;
    }
    ret += go(idx+1, sum+a[idx+1]);
    ret += go(idx+1, sum-a[idx+1]);
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) cin >> a[i];

    cout << go(0, a[0]) << '\n';

    return 0;
}