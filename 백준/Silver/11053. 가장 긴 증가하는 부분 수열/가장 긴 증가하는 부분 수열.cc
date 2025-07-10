#include <bits/stdc++.h>
using namespace std;

const int MAX = 1004;
int N, num, ret, a[MAX];

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%d", &num);
        auto lowerPos = lower_bound(a, a+ret, num);
        if (*lowerPos == 0) ret++;
        *lowerPos = num;
    }
    cout << ret << '\n';

    return 0;
}