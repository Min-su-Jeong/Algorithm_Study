#include <bits/stdc++.h>
using namespace std;

int N, M, ret, a[15004];

void solve() {
    for (int i=0; i<N; i++) {
        for (int j=0; j<i; j++) {
            if (a[i]+a[j] == M) ret++;
        }
    }
}

int main() {
    cin >> N;
    cin >> M;
    for (int i=0; i<N; i++) cin >> a[i];

    solve();
    
    cout << ret << '\n';
    return 0;
}