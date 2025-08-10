#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int MAX = 1004;
int T, n, m, a[MAX], b[MAX];
ll ret;
vector<int> sumA, sumB;

int main() {
    scanf("%d", &T);
    scanf("%d", &n);
    for (int i=0; i<n; i++) scanf("%d", a+i);
    scanf("%d", &m);
    for (int i=0; i<m; i++) scanf("%d", b+i);

    for (int i=0; i<n; i++) {
        int sum = a[i];
        sumA.push_back(sum);
        for (int j=i+1; j<n; j++) {
            sum += a[j];
            sumA.push_back(sum);
        }
    }

    for (int i=0; i<m; i++) {
        int sum = b[i];
        sumB.push_back(sum);
        for (int j=i+1; j<m; j++) {
            sum += b[j];
            sumB.push_back(sum);
        }
    }

    sort(sumB.begin(), sumB.end());
    for (int num: sumA) {
        int target = T - num;
        int lb = lower_bound(sumB.begin(), sumB.end(), target) - sumB.begin();
        int ub = upper_bound(sumB.begin(), sumB.end(), target) - sumB.begin();
        ret += (ub - lb);
    }
    printf("%lld", ret);

    return 0;
}