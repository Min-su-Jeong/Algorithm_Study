#include <bits/stdc++.h>
using namespace std;

int N, y, x, ret;

int main() {
    scanf("%d", &N);
    vector<pair<int, int>> v;
    for (int i=0; i<N; i++) {
        scanf("%d %d", &x, &y);
        v.push_back({x, y});
    }
    sort(v.begin(), v.end());

    int l = v[0].first;
    int r = v[0].second;
    for (int i=1; i<v.size(); i++) {
        if (r < v[i].first) {
            ret += r-l;
            l = v[i].first;
            r = v[i].second;
        }
        else if (r >= v[i].first && r < v[i].second) {
            r = v[i].second;
        }
    }
    ret += r-l;
    cout << ret << '\n';
    
    return 0;
}