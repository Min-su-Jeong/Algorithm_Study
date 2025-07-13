#include <bits/stdc++.h>
using namespace std;

int N, M, ret;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    vector<int> v(N);
    for (int i=0; i<N; i++) cin >> v[i];

    if (M > 200000) cout << 0 << '\n';
    else {
        int l = 0;
        int r = v.size()-1;
        sort(v.begin(), v.end());

        while (l < r) {
            if (v[l] + v[r] > M) r--;
            else if (v[l] + v[r] == M) ret++, l++;
            else l++;
        }
        cout << ret << '\n';
    }
    return 0;
}