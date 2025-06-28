#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;
int N, mp, mf, ms, mv, p, f, s, v, sum, ret=INF;
struct A {
    int mp, mf, ms, mv, cost;
} a[16];
map<int, vector<vector<int>>> ret_v;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> N;
    cin >> mp >> mf >> ms >> mv;
    for (int i=0; i<N; i++) {
        cin >> a[i].mp >> a[i].mf >> a[i].ms >> a[i].mv >> a[i].cost;
    }

    for (int i=0; i<(1 << N); i++) {
        p = f = s = v = sum = 0;
        vector<int> vec;
        for (int j=0; j<N; j++) {
            if (i & (1 << j)) {
                vec.push_back(j+1);
                p += a[j].mp;
                f += a[j].mf;
                s += a[j].ms;
                v += a[j].mv;
                sum += a[j].cost;
            }
        }
        if (p >= mp && f >= mf && s >= ms && v >= mv) {
            if (ret >= sum) {
                ret = sum;
                ret_v[ret].push_back(vec);
            }
        }
    }
    if (ret == INF) cout << -1 << '\n';
    else {
        sort(ret_v[ret].begin(), ret_v[ret].end());
        cout << ret << '\n';
        for (int i: ret_v[ret][0]) {
            cout << i << ' ';
        }
    }
    return 0;
}