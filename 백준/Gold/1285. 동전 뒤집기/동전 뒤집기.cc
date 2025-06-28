#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;
int N, a[44], ret=INF;
string s;

void go(int level) {
    if (level == N+1) {
        int sum = 0;
        for (int i=1; i<= (1 << (N-1)); i*=2) {
            int cnt = 0;
            for (int j=1; j<=N; j++) if (a[j] & i) cnt++;
            sum += min(cnt, N-cnt);
        }
        ret = min(ret, sum);
        return;
    }
    go(level+1);
    a[level] = ~a[level];
    go(level+1);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=1; i<=N; i++) {
        cin >> s;
        int k = 1;
        for (int j=0; j<s.size(); j++) {
            if (s[j] == 'T') a[i] |= k;
            k *= 2;
        }
    }

    go(1);
    cout << ret << '\n';

    return 0;
}