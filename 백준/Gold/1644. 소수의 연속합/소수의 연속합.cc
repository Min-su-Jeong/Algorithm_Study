#include <bits/stdc++.h>
using namespace std;

const int MAX = 4000001;
int N, a[2000001], p, sum, l, r, ret; 
bool notPrime[MAX];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=2; i*i<=N; ++i) {
        if (notPrime[i]) continue;
        for (int j=i*i; j<=N; j+=i) notPrime[j] = 1;
    }

    for (int i=2; i<=N; i++) {
        if (!notPrime[i]) a[p++] = i;
    }

    while (true) {
        if (sum >= N) sum -= a[l++];
        else if (r == p) break;
        else sum += a[r++];
        if (sum == N) ret++;
    }
    cout << ret << '\n';
    return 0;
}