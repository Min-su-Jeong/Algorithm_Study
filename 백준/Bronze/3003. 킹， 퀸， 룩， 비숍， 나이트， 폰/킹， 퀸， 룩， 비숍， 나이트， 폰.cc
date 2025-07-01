#include <bits/stdc++.h>
using namespace std;

int n, a[11] = {1, 1, 2, 2, 2, 8};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    for (int i=0; i<6; i++) {
        cin >> n;
        cout << a[i] - n << ' ';
    }
    return 0;
}