#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll A, B, C;

ll modular(ll a, ll b) {
    if (b == 1) return a % C;

    ll ret = modular(a, b/2);
    ret = (ret * ret) % C;

    if (b % 2) ret = (ret * a) % C;

    return ret;
}

int main() {
    scanf("%lld %lld %lld", &A, &B, &C);
    cout << modular(A, B) << '\n';
    return 0;
}