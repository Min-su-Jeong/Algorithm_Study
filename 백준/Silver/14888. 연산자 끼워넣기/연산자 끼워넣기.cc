#include <bits/stdc++.h>
using namespace std;

int N, pl, mi, mu, di, a[12];
int mn = INT_MAX, mx = INT_MIN;

void go(int depth, int sum, int pl, int mi, int mu, int di) {
    if (depth == N-1) {
        mn = min(mn, sum);
        mx = max(mx, sum);
        return;
    }
    if (pl) go(depth+1, sum+a[depth+1], pl-1, mi, mu, di);
    if (mi) go(depth+1, sum-a[depth+1], pl, mi-1, mu, di);
    if (mu) go(depth+1, sum*a[depth+1], pl, mi, mu-1, di);
    if (di) go(depth+1, sum/a[depth+1], pl, mi, mu, di-1);
    return;
}

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) scanf("%d", &a[i]);
    scanf("%d %d %d %d", &pl, &mi, &mu, &di);

    go(0, a[0], pl, mi, mu, di);

    cout << mx << '\n' << mn << '\n';
    return 0;
}