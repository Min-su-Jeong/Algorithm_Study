#include <bits/stdc++.h>
using namespace std;

int X, N, a, b, sum;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> X >> N;
    for (int i=0; i<N; i++) {
        cin >> a >> b;
        sum += a*b;
    }
    if (sum == X) cout << "Yes\n";
    else cout << "No\n";
}