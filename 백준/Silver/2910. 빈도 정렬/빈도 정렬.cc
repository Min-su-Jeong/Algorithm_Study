#include <bits/stdc++.h>
using namespace std;

const int MAX = 1004;
int N, C, a[MAX];
map<int, int> mp, mp_first;
vector<pair<int, int>> v;

bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.first == b.first) {
        return mp_first[a.second] < mp_first[b.second];
    }
    return a.first > b.first;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> C;
    for (int i=0; i<N; i++) {
        cin >> a[i]; mp[a[i]]++;
        if (mp_first[a[i]] == 0) mp_first[a[i]] = i+1;
    }

    for (auto it: mp) v.push_back({it.second, it.first});
    sort(v.begin(), v.end(), cmp);

    for (auto it: v) {
        while(it.first--) cout << it.second << ' ';
    }
    return 0;
}