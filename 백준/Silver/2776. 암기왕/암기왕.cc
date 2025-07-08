#include <bits/stdc++.h>
using namespace std;

int T, N, M;

bool check(int target, vector<int> &v) {
    int lo = 0, hi = v.size()-1, mid;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (target < v[mid]) hi = mid - 1;
        else if (target == v[mid]) return 1;
        else lo = mid + 1;
    }
    return 0;
}

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
            if (check(b[i], a)) cout << "1\n";
            else cout << "0\n";
        }
    }
    return 0;
}