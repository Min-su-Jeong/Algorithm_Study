#include <bits/stdc++.h>
using namespace std;

int N, len, lis[101];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    vector<pair<int, int>> v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i].first >> v[i].second;
    }
    sort(v.begin(), v.end());

    for (int i=0; i<N; i++) {
        auto lowerPos = lower_bound(lis, lis+len, v[i].second);
        int pos = lowerPos - lis;
        if (*lowerPos == 0) len++;
        *lowerPos = v[i].second;
    }
    cout << N - len << '\n';
    
    return 0;
}