#include <bits/stdc++.h>
using namespace std;

const int MAX = 1004;
int m, n, order, ret;
int a[MAX], b[MAX], psumA[2*MAX], psumB[2*MAX];
map<int, int> cntA, cntB;

void make(int n, int psum[], map<int, int> &cnt) {
    for (int interval=1; interval<=n; interval++) {
        for (int start=interval; start<=n+interval-1; start++) {
            int sum = psum[start] - psum[start-interval];
            cnt[sum]++;
            if (interval == n) break;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> order >> m >> n;
    for (int i=1; i<=m; i++) {
        cin >> a[i];
        psumA[i] = psumA[i-1] + a[i];
    }
    for (int i=m+1; i<=2*m; i++) psumA[i] = psumA[i-1] + a[i-m];

    for (int i=1; i<=n; i++) {
        cin >> b[i];
        psumB[i] = psumB[i-1] + b[i];
    }
    for (int i=n+1; i<=2*n; i++) psumB[i] = psumB[i-1] + b[i-n];

    make(m, psumA, cntA);
    make(n, psumB, cntB);

    ret = cntA[order] + cntB[order];
    for (int i=1; i<order; i++) {
        ret += (cntA[i] * cntB[order-i]);
    }
    cout << ret << '\n';
    return 0;
}