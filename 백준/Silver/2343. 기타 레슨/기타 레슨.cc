#include <bits/stdc++.h>
using namespace std;

const int MAX = 100001;
int N, M, mx, sum, ret, a[MAX];

bool check(int mid) {
    if (mid < mx) return false;
    int tmp = mid;
    int cnt = 0;
    for (int i=0; i<N; i++) {
        if (mid - a[i] < 0) {
            mid = tmp;
            cnt++;
        }
        mid -= a[i];
    }
    if (mid != tmp) cnt++;
    return cnt <= M;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> a[i];
        sum += a[i];
        mx = max(mx, a[i]);
    }

    int l=0, r=sum;
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