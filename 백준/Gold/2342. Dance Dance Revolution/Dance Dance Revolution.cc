#include <bits/stdc++.h>
using namespace std;

const int MAX = 100001;
int num, N, a[MAX], dp[5][5][MAX];
vector<int> v;

int check(int from, int to) {
    if (from == 0) return 2;
    if (from == to) return 1;
    if (abs(from - to) == 2) return 4;
    return 3;
}

int solve(int y, int x, int target) {
    if (target == N) return 0;
    if (dp[y][x][target] != -1) return dp[y][x][target];

    int left = solve(v[target], x, target+1) + check(y, v[target]);
    int right = solve(y, v[target], target+1) + check(x, v[target]);
    return dp[y][x][target] = min(left, right);
}

int main() {
    memset(dp, -1, sizeof(dp));

    while (true) {
        scanf("%d", &num);
        if (num == 0) break;
        v.push_back(num);
    }
    
    N = v.size();
    printf("%d\n", solve(0, 0, 0));

    return 0;
}