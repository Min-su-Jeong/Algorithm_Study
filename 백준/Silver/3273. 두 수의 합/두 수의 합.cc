#include <bits/stdc++.h>
using namespace std;

int n, x, ret;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    vector<int> v(n);
    for (int i=0; i<n; i++) cin >> v[i];
    cin >> x;

    sort(v.begin(), v.end());

    int l = 0, r = n-1;
    while (l < r) {
        int sum = v[l] + v[r];
        if (sum == x) r--, ret++;
        else if (sum < x) l++;
        else if (sum > x) r--;
    }
    cout << ret << '\n';
    
    return 0;
}