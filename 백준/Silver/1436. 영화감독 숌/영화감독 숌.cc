#include <bits/stdc++.h>
using namespace std;

int N;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    int ret = 666;
    for (;;ret++) {
        if (to_string(ret).find("666") != string::npos) N--;
        if (N == 0) break;
    }
    cout << ret << '\n';
    return 0;
}