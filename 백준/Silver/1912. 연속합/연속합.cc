#include <bits/stdc++.h>
using namespace std;

int n, a, sum, ret=-1000;

int main() {
    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        scanf("%d", &a);
        sum += a;
        ret = max(ret, sum);
        if (sum < 0) sum = 0;
    }
    printf("%d", ret);

    return 0;
}