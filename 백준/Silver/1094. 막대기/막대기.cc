#include <bits/stdc++.h>
using namespace std;

int X, ret=1;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> X;
    while (X != 1) {
        if (1 & X) ret++;
        X /= 2;
    }
    cout << ret << '\n';
    return 0;
}