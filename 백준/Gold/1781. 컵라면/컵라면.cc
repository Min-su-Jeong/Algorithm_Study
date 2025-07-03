#include <bits/stdc++.h>
using namespace std;

int N, d, r, ret;
vector<pair<int, int>> v;
priority_queue<int, vector<int>, greater<int>> pq;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> d >> r;
        v.push_back({d, r});
    }
    sort(v.begin(), v.end());

    for (int i=0; i<N; i++) {
        ret += v[i].second;
        pq.push(v[i].second);
        if (pq.size() > v[i].first) {
            ret -= pq.top();
            pq.pop();
        }
    }
    cout << ret << '\n';
    return 0;
}