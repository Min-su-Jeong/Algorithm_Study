
#include <bits/stdc++.h>
using namespace std;

const int MAX = 101;
int N, L[MAX], J[MAX], dp[MAX];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) cin >> L[i];
    for (int i=0; i<N; i++) cin >> J[i];
    for (int i=0; i<N; i++) {
        for (int j=100; j>L[i]; j--) {
            dp[j] = max(dp[j], dp[j - L[i]] + J[i]);
        }
    }
    cout << dp[100] << '\n';
    return 0;
}