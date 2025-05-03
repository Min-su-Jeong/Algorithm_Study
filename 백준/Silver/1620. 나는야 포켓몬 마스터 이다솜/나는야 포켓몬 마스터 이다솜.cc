#include <bits/stdc++.h>
using namespace std;

string s, a[100004];
int N, M;
map<string, int> mp;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;

    for (int i=0; i<N; i++) {
        cin >> s;
        mp[s] = i+1;
        a[i+1] = s;
    }
    for (int i =0; i<M; i++) {
        cin >> s;
        if (atoi(s.c_str()) == 0) {
            cout << mp[s] << "\n";
        } else {
            cout << a[atoi(s.c_str())] << "\n";
        }
    }

    return 0;
}