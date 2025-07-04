#include <bits/stdc++.h>
using namespace std;

int N, a, b, ret;
vector<pair<int, int>> v;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> a >> b;
        v.push_back({a, b});
    }
    sort(v.begin(), v.end());
    
    for (int i=0; i<N; i++) {
        int process = v[i].first + v[i].second;
        if (ret > v[i].first) {
            ret += v[i].second;
        } else {
            ret = process;
        } 
    }
    cout << ret << '\n';

    return 0;
}