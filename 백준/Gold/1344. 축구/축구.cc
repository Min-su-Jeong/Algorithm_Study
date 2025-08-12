#include <bits/stdc++.h>
using namespace std;

const int MAX = 20;
double A, B, dp[MAX][MAX][MAX];
bool prime[MAX];

double go(int idx, int x, int y) {
    if (idx == 18) return prime[x] || prime[y] ? 1.0 : 0.0;
    double &ret = dp[idx][x][y];
    if (ret > -0.5) return ret;
    ret = 0.0;
    ret += go(idx+1, x+1, y) * A * (1-B);
    ret += go(idx+1, x+1, y+1) * A * B;
    ret += go(idx+1, x, y+1) * (1-A) * B;
    ret += go(idx+1, x, y) * (1-A) * (1-B);
    return ret;
}

void isPrime() {
    fill(prime, prime+MAX, 1);
    prime[0] = 0; prime[1] = 0;
    for (int i=2; i<=MAX; i++) {
        for (int j=i+i; j<=MAX; j+=i) {
            prime[j] = 0;
        }
    }
}

int main() {
    scanf("%lf %lf", &A, &B);
    A /= 100; B /= 100;
    
    isPrime();

    memset(dp, -1, sizeof(dp));
    printf("%.6lf", go(0, 0, 0));
    
    return 0;
}