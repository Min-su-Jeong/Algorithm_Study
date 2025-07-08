#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll X, Y, mid, ret=-1;

int main() {
    scanf("%lld %lld", &X, &Y);

    ll Z = Y * 100 / X;
    ll lo = 1, hi=1e9;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if ((Y + mid) * 100 / (X + mid) > Z) {
            ret = mid;
            hi = mid - 1;
        } else lo = mid + 1; 
    }
    cout << ret << '\n';

    return 0;
}