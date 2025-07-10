#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 1000004;
const int INF = 1e9 + 4;
int N, num, cnt, lis[MAX_N];
pair<int, int> ret[MAX_N];
vector<int> v;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    fill(lis, lis + MAX_N, INF);
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> num;
        auto lowerPos = lower_bound(lis, lis + i, num);
        int pos = (int)(lowerPos - lis);
        if (*lowerPos == INF) cnt++;
        *lowerPos = num;
        ret[i].first = pos;
        ret[i].second = num;
    }

    for (int i=N-1; i>=0; i--) {
        if (ret[i].first == cnt-1) {
            v.push_back(ret[i].second);
            cnt--;
        }
    }
    reverse(v.begin(), v.end());

    cout << v.size() << '\n';
    for (int i: v) cout << i << ' ';

    return 0;
}