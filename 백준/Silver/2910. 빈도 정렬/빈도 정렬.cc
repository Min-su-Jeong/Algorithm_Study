#include <bits/stdc++.h>
using namespace std;

int N, C, a[1004];
map<int, int> mp, mp_first;
vector<pair<int, int>> v;

bool cmp(pair<int, int> a, pair<int, int> b) {
    if (a.second == b.second) return mp_first[a.first] < mp_first[b.first];
    return a.second > b.second;
}

int main() {
    scanf("%d %d", &N, &C);
    for (int i=0; i<N; i++) {
        scanf("%d", a+i);
        mp[a[i]]++;
        if (mp_first[a[i]] == 0) mp_first[a[i]] = i+1;
    }

    for (auto it: mp) v.push_back({it.first, it.second});
    sort(v.begin(), v.end(), cmp);

    for (auto it: v) {
        for (int i=0; i<it.second; i++) {
            cout << it.first << ' ';
        }
    }
    return 0;
}