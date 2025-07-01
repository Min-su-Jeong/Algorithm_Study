#include <bits/stdc++.h>
using namespace std;

int n;
bool check[31];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    for (int i=0; i<28; i++) {
        cin >> n;
        check[n] = 1;
    }

    for (int i=1; i<=30; i++) {
        if (!check[i]) cout << i << '\n';
    }
    return 0;
}