#include <bits/stdc++.h>
using namespace std;

int N, M, ret, a[15004];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N >> M;
    for (int i=0; i<N; i++) cin >> a[i];

    if (M > 200000) cout << 0 << "\n";
    else {
        for (int i=0; i<N; i++) {
            for (int j=i+1; j<N; j++) {
                if (a[i] + a[j] == M) ret++;
            }
        }
        cout << ret << "\n";
    }
    return 0;
}