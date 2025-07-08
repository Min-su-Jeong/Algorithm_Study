#include <bits/stdc++.h>
using namespace std;

int T, N, M;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> T;
    while (T--) {
        cin >> N >> M;

        int ret = 0;
        vector<int> a(N), b(M);
        for (int i=0; i<N; i++) cin >> a[i];
        for (int i=0; i<M; i++) cin >> b[i];
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        for (int i=0; i<N; i++) {
            int pos = lower_bound(b.begin(), b.end(), a[i]) - b.begin();
            ret += pos;
        }
        cout << ret << '\n';
    }
    return 0;
}