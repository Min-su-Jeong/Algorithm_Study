#include <bits/stdc++.h>
using namespace std;

int N, a[2000001], p, l, r, sum, ret;
bool prime[4000001];

int main() {
    memset(prime, true, sizeof(prime));
    scanf("%d", &N);
    for (int i=2; i*i<=N; ++i) {
        if (!prime[i]) continue;
        for (int j=i*i; j<=N; j+=i) {
            prime[j] = 0;
        }
    }

    for (int i=2; i<=N; i++) {
        if (prime[i]) a[p++] = i;
    }

    while(true) {
        if (sum >= N) sum -= a[l++];
        else if (r == p) break;
        else sum += a[r++];
        if (sum == N) ret++;
    }

    cout << ret << '\n';
    return 0;
}