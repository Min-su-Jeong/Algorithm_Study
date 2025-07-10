#include <bits/stdc++.h>
using namespace std;

const int MAX = 10004;
int N;
double mx, a[MAX], dp[MAX];

int main() {
    scanf("%d", &N);
    for (int i=0; i<N; i++) {
        scanf("%lf", &a[i]);
    }
    
    dp[0] = a[0];
    for (int i=1; i<N; i++) {
        dp[i] = max(a[i], a[i]*dp[i-1]);
        mx = max(mx, dp[i]);
    }
    printf("%.3f", mx);
    
    return 0;
}