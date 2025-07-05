#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX = 100001;
ll N, l, r, ret, a[MAX], cnt[MAX];

int main() {
    scanf("%lld", &N);
    for (int i=0; i<N; i++) scanf("%lld", a + i);

    while (r < N) {
        if (!cnt[a[r]]) {
            cnt[a[r]]++;
            r++;
        } else {
            ret += (r - l);
            cnt[a[l]]--;
            l++;
        }
    }
    ret += (ll)(r - l) * (r - l + 1) / 2;
    printf("%lld", ret);

    return 0;
}