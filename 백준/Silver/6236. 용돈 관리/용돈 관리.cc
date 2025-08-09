#include <bits/stdc++.h>
using namespace std;

const int MAX = 100004;
int N, M, mx, ret, a[MAX];

bool check(int mid) {
    int cnt = 1, tmp = mid;
    for (int i=0; i<N; i++) {
        if (mid - a[i] < 0) {
            mid = tmp;
            cnt++;
        }
        mid -= a[i];
    }
    return M >= cnt;
}

int main() {
    scanf("%d %d", &N, &M);
    for (int i=0; i<N; i++) {
        scanf("%d", a+i);
        mx = max(mx, a[i]);
    }

    int l = mx, r = 100000 * 10000 + 4;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (check(mid)) {
            ret = mid;
            r = mid - 1;
        } else l = mid + 1;
    }
    cout << ret << '\n';
    return 0;
}