#include <bits/stdc++.h>
using namespace std;

int N, C, ret, a[31];
vector<int> v1, v2;

void go(int here, int n, vector<int> &v, int sum) {
    if (sum > C) return;
    if (here > n) {
        v.push_back(sum);
        return;
    }
    go(here+1, n, v, sum+a[here]);
    go(here+1, n, v, sum);
    return;
}

int main() {
    scanf("%d %d", &N, &C);
    for (int i=0; i<N; i++) scanf("%d", &a[i]);

    go(0, N/2-1, v1, 0);
    go(N/2, N-1, v2, 0);

    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());

    for (int i: v1) {
        if (C - i >= 0) {
            ret += ((int)(upper_bound(v2.begin(), v2.end(), C-i) - v2.begin()));
        }
    }
    printf("%d", ret);
    return 0;
}