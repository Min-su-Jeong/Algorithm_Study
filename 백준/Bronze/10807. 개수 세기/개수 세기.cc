#include <bits/stdc++.h>
using namespace std;

int N, d, v;
map<int, int> mp;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> d;
        mp[d]++;
    }
    cin >> v;
    cout << mp[v] << '\n';
    
    return 0;
}