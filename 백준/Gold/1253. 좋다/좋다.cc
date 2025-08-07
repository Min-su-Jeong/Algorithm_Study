#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int ret;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N;
    cin >> N;

    vector<ll> a(N);
    for (int i=0; i<N; i++) cin >> a[i];
    sort(a.begin(), a.end());

    for (int i=0; i<N; i++) {
        int l = 0, r = N-1;
        while (l < r) {
            if (i == l) {
                l++;
                continue;
            }
            if (i == r) {
                r--;
                continue;
            }

            ll sum = a[l] + a[r];

            if (sum == a[i]) {
                ret++;
                break;
            }
            else if (sum < a[i]) l++;
            else r--;
        }
    }
    cout << ret << '\n';
    return 0;
}