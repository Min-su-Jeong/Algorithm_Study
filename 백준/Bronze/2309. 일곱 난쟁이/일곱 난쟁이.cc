#include <bits/stdc++.h>
using namespace std;

int a[10], sum;
vector<int> v;
pair<int, int> ret;

void solution() {
    for (int i=0; i<9; i++) {
        for (int j=0; j<i; j++) {
            if (sum - a[i] - a[j] == 100) {
                ret = {i, j};
                return;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);

    for (int i=0; i<9; i++) {
        cin >> a[i];
        sum += a[i];
    }
    solution();

    for (int i=0; i<9; i++) {
        if (ret.first == i || ret.second == i) continue;
        v.push_back(a[i]);
    }

    sort(v.begin(), v.end());

    for (int i: v) cout << i << ' ';

    return 0;
}