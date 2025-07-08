#include <bits/stdc++.h>
using namespace std;

int T, N, M;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> T;
    while (T--) {
        cin >> N;
        vector<int> a(N);
        for (int i=0; i<N; i++) cin >> a[i];
        sort(a.begin(), a.end());

        cin >> M;
        vector<int> b(M);
        for (int i=0; i<M; i++) {
            cin >> b[i];
            int pos = lower_bound(a.begin(), a.end(), b[i]) - a.begin();
            if (a[pos] == b[i]) cout << "1\n";
            else cout << "0\n";
        }
    }
    return 0;
}